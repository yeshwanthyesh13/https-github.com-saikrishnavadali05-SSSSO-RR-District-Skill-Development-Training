import httpx
import html
from fastapi import HTTPException
from ..models.schemas import Question
from ..data.db import quiz_db


async def import_questions_from_api(amount, category, difficulty):
    url = f"https://opentdb.com/api.php?amount={amount}&difficulty={difficulty}&type=multiple"
    if category:
        url += f"&category={category}"

    async with httpx.AsyncClient() as client:
        response = await client.get(url)
        data = response.json()

    if data["response_code"] != 0:
        raise HTTPException(status_code=500, detail="Failed to fetch trivia questions")

    new_questions = []
    for item in data["results"]:
        all_options = item["incorrect_answers"] + [item["correct_answer"]]
        shuffled = sorted([html.unescape(opt) for opt in all_options])

        question_data = Question(
            id=len(quiz_db) + 1,
            question=html.unescape(item["question"]),
            options=shuffled,
            correct_answer=html.unescape(item["correct_answer"]),
            category=item["category"],
            difficulty=item["difficulty"]
        )
        quiz_db.append(question_data)
        new_questions.append(question_data)

    return {"imported": len(new_questions), "questions": new_questions}

def get_filtered_questions(category=None, difficulty=None):
    results = quiz_db
    if category:
        results = [q for q in results if q.category.lower() == category.lower()]
    if difficulty:
        results = [q for q in results if q.difficulty.lower() == difficulty.lower()]
    return results

def get_question_by_id(qid):
    for question in quiz_db:
        if question.id == qid:
            return question
    return None
