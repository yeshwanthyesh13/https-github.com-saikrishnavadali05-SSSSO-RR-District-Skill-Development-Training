from fastapi import FastAPI
from routers import auth, quiz, score

app = FastAPI()

# Include all routers
app.include_router(auth.router)
app.include_router(quiz.router)
app.include_router(score.router)

@app.get("/")
def read_root():
    return {"message": "Welcome to the FastAPI Trivia Quiz! 🎉 Visit /docs to try it out."}
