from fastapi import FastAPI
from uvicorn import run
from app.api import auth_router

app = FastAPI(
    title="FastAPI Messenger",
    description="FastAPI Messenger written in Python",
    version="1.0.0",
)

app.include_router(auth_router.router, prefix="/auth", tags=["Auth"])

if __name__ == "__main__":
    run("main:app", host="127.0.0.1", port=8000)
