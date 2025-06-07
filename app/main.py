from fastapi import FastAPI
from app.db.session import get_db

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello, FastAPI!"}