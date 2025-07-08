from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, func
from app.models.emotion_entry import EmotionEntry
from app.schemas.emotion_entry import EmotionEntryCreate
from typing import List, Dict
from datetime import datetime
from collections import defaultdict
import uuid


async def create_emotion_entry(
    db: AsyncSession,               # FastAPI에서 Depends(get_db)로 주입되는 DB 세션
    entry: EmotionEntryCreate       # 사용자가 보낸 요청(JSON)을 파싱한 Pydantic 객체
) -> EmotionEntry:
    # EmotionEntry는 SQLAlchemy 모델이므로, entry(Pydantic 객체)를 기반으로 새 객체 생성
    new_entry = EmotionEntry(
        id=uuid.uuid4(),  # 기본키 수동 생성 (DB에서 자동 생성 안 하므로)
        user_session_id=entry.user_session_id,
        emotion=entry.emotion,
        time_type=entry.time_type,
        timestamp=entry.timestamp,
        target_time=entry.target_time
    )

    db.add(new_entry)         # 세션에 추가
    await db.commit()         # DB에 커밋
    await db.refresh(new_entry)  # 생성된 객체를 다시 읽어옴 (id 등 포함)

    return new_entry


async def get_emotion_summary_by_session(
    db: AsyncSession,
    user_session_id: str,
    time_type: str
) -> Dict[str, int]:
    result = await db.execute(
        select(EmotionEntry.emotion, func.count())
        .where(
            EmotionEntry.user_session_id == user_session_id,
            EmotionEntry.time_type == time_type
        )
        .group_by(EmotionEntry.emotion)
    )
    return {emotion: count for emotion, count in result.all()}


async def summarize_emotion_by_time(
    db: AsyncSession,
    qr_group_id: str,
    time_type: str
) -> Dict[str, Dict[str, int]]:
    result = await db.execute(
        select(EmotionEntry.timestamp, EmotionEntry.emotion)
        .where(
            EmotionEntry.qr_group_id == qr_group_id,
            EmotionEntry.time_type == time_type
        )
    )
    
    summary = defaultdict(lambda: defaultdict(int))
    for timestamp, emotion in result.all():
        hour_str = timestamp.strftime("%Y-%m-%d %H:00")
        summary[hour_str][emotion] += 1
        
    return summary
