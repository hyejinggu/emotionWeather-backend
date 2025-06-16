from fastapi import FastAPI
from app.api import emotion, qr

app = FastAPI()

# 서버 실행: uvicorn app.main:app --reload
@app.get("/")
def read_root():
    return {"message": "Hello, FastAPI!"}

app.include_router(emotion.router)
app.include_router(qr.router)
