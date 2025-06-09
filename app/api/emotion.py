from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from app.db.session import get_db
from app.schemas.emotion_entry import EmotionEntryCreate, EmotionEntryRead
from app.services.emotion_service import create_emotion_entry

router = APIRouter()

# @router.post(...): 이 함수가 /emotion 경로의 POST 요청을 처리
# response_model=EmotionEntryRead: 이 함수의 반환값을 자동으로 JSON으로 직렬화 (필드 검증 포함)
# entry: EmotionEntryCreate: FastAPI가 요청 body(JSON)를 자동으로 이 타입으로 변환
# db: AsyncSession = Depends(get_db): DB 세션 주입 (비동기 방식)
# return await create_emotion_entry(...): 실제 저장을 담당하는 서비스 함수 호출
@router.post("/emotion", response_model=EmotionEntryRead)
async def submit_emotion(
    entry: EmotionEntryCreate,
    db: AsyncSession = Depends(get_db)
):
    return await create_emotion_entry(db, entry)
