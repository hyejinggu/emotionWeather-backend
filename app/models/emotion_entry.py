import uuid
from datetime import datetime
from sqlalchemy import Column, TIMESTAMP, TEXT
from sqlalchemy.dialects.postgresql import UUID, JSON
from app.db.base import Base

class EmotionEntry(Base):
    __tablename__ = "emotion_entry"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)

    # 어떤 사용자(session)가 작성한 감정인지
    user_session_id = Column(UUID(as_uuid=True), nullable=False)
    
    # 어떤 qr group에서 작성된 감정인지
    qr_group_id = Column(UUID(as_uuid=True), nullable=False)

    # 감정 이모지 (예: 😄)
    emotion = Column(TEXT, nullable=False)

    # 현재/미래 감정 구분 ('current', 'future')
    time_type = Column(TEXT, nullable=False)

    # 감정 입력 시각
    timestamp = Column(TIMESTAMP, nullable=False)

    # 미래 감정일 경우의 예측 시간
    target_time = Column(TIMESTAMP, nullable=True)
