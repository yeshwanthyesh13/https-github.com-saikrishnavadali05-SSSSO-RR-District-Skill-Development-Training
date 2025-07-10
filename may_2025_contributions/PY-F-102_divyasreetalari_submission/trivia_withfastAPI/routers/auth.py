from fastapi import APIRouter, HTTPException
from models.schemas import UserLogin
from data import users_db
from passlib.context import CryptContext
import json
import os

router = APIRouter()

# Password hasher
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# Register route
@router.post("/register/")
def register(user: UserLogin):
    if user.username in users_db:
        raise HTTPException(status_code=400, detail="Username already exists")

    hashed_password = pwd_context.hash(user.password)
    users_db[user.username] = hashed_password

    # Save to users.json
    with open("users.json", "w") as f:
        json.dump(users_db, f, indent=4)

    return {"message": f"User {user.username} registered successfully"}

# Login route
@router.post("/login/")
def login(user: UserLogin):
    stored_password = users_db.get(user.username)
    if not stored_password:
        raise HTTPException(status_code=401, detail="Invalid username or password")

    if not pwd_context.verify(user.password, stored_password):
        raise HTTPException(status_code=401, detail="Invalid username or password")

    return {"message": f"User {user.username} logged in successfully"}
