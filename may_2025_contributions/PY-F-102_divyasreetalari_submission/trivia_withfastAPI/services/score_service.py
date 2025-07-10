import os
import json
from fastapi import HTTPException
from models.schemas import Answer
from services.quiz_service import get_question_by_id
from data.db import scores_db, users_db


# Load scores from JSON when app starts
if os.path.exists("data/scores.json"):
    with open("data/scores.json", "r") as f:
        scores_db.update(json.load(f))

# Save scores to JSON file
def save_scores_to_file():
    with open("data/scores.json", "w") as f:
        json.dump(scores_db, f, indent=4)

# Validate current user (used in Depends)
def get_current_user(username: str):
    if username not in users_db:
        raise HTTPException(status_code=401, detail="Invalid user")
    return username

# Check answer, update score, and return result
def update_score(answer: Answer, username: str):
    question = get_question_by_id(answer.question_id)
    if not question:
        raise HTTPException(status_code=404, detail="Question not found")

    is_correct = question.correct_answer == answer.answer

    # Initialize score if user is new
    if username not in scores_db:
        scores_db[username] = 0

    if is_correct:
        scores_db[username] += 1

    save_scores_to_file()

    return {
        "your_answer": answer.answer,
        "correct_answer": question.correct_answer,
        "result": "Correct" if is_correct else "Wrong",
        "score": scores_db[username]
    }
