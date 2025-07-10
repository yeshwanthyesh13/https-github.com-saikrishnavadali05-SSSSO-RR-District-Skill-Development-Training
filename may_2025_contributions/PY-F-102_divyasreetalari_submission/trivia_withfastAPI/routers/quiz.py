from fastapi import APIRouter, Depends
from models.schemas import Answer
from services.quiz_service import (
    import_questions_from_api,
    get_filtered_questions,
    get_question_by_id
)
from services.score_service import update_score, get_current_user

router = APIRouter()

@router.get("/import-questions/")
async def import_questions(amount: int = 10, category: int = None, difficulty: str = "easy"):
    return await import_questions_from_api(amount, category, difficulty)

@router.get("/questions/")
def get_questions(category: str = None, difficulty: str = None):
    return get_filtered_questions(category, difficulty)

@router.post("/answer/")
def submit_answer(answer: Answer, username: str = Depends(get_current_user)):
    return update_score(answer, username)
