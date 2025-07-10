from pydantic import BaseModel, ConfigDict
from typing import List

# ✅ Model for user input (register/login)
class UserLogin(BaseModel):
    username: str
    password: str

    model_config = ConfigDict(
        json_schema_extra={
            "example": {
                "username": "john_doe",
                "password": "secret123"
            }
        }
    )

# ✅ Optional: model for response without password
class UserPublic(BaseModel):
    username: str

# ✅ Question schema for quiz data
class Question(BaseModel):
    id: int
    question: str
    options: List[str]
    correct_answer: str
    category: str
    difficulty: str

# ✅ Schema for answer submission
class Answer(BaseModel):
    question_id: int
    answer: str
