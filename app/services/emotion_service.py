from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from app.models.emotion_entry import EmotionEntry
from app.schemas.emotion_entry import EmotionEntryCreate
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
