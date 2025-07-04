from fastapi import FastAPI
from app.api import emotion, qr
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()

# CORS 설정 추가
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],  # 또는 ["*"]로 전체 허용 가능
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 가상환경 활성화 
# window: venv\Scripts\activate
# mac: source venv/bin/activate
# 패키지 설치: pip install -r requirements.txt
# 서버 실행: uvicorn app.main:app --reload
@app.get("/")
def read_root():
    return {"message": "Hello, FastAPI!"}

app.include_router(emotion.router)
app.include_router(qr.router)
