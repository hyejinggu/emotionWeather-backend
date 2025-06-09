from fastapi import FastAPI
from app.api import emotion 

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello, FastAPI!"}

app.include_router(emotion.router)