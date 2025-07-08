from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from app.db.session import get_db
from app.schemas.emotion_entry import EmotionEntryCreate, EmotionEntryRead
from app.services.emotion_service import create_emotion_entry, summarize_emotion_by_time
from app.services.openai_service import get_ai_feedback
from datetime import datetime
from app.schemas.ai_feedback import EmotionSummaryResponse


router = APIRouter()

# @router.post(...): 이 함수가 /emotion 경로의 POST 요청을 처리
# response_model=EmotionEntryRead: 이 함수의 반환값을 자동으로 JSON으로 직렬화 (필드 검증 포함)
# entry: EmotionEntryCreate: FastAPI가 요청 body(JSON)를 자동으로 이 타입으로 변환
# db: AsyncSession = Depends(get_db): DB 세션 주입 (비동기 방식)
# return await create_emotion_entry(...): 실제 저장을 담당하는 서비스 함수 호출
@router.post("/emotion/save", response_model=EmotionEntryRead)
async def submit_emotion(
    entry: EmotionEntryCreate,
    db: AsyncSession = Depends(get_db)
):
    return await create_emotion_entry(db, entry) 


@router.get("/emotion/summary", response_model=EmotionSummaryResponse)
async def emotion_summary(
    qr_group_id: str,
    db: AsyncSession = Depends(get_db)
):
    summary = await summarize_emotion_by_time(db, qr_group_id, "future")
    feedback = await get_ai_feedback(summary, datetime.now())
    
    return {
        "summary": summary,
        "feedback": feedback
    }
