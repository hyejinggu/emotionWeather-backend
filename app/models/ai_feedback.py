import uuid
from datetime import datetime
from sqlalchemy import Column, TIMESTAMP, TEXT
from sqlalchemy.dialects.postgresql import UUID, JSON
from app.db.base import Base

class AIFeedback(Base):
    __tablename__ = "ai_feedback"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)

    # 어떤 그룹(qr_group)에 대한 응답인지
    qr_group_id = Column(UUID(as_uuid=True), nullable=False)

    # 응답이 생성된 시간
    generated_at = Column(TIMESTAMP, nullable=False, default=datetime.utcnow)

    # 감정 통계 (예: {"😄": 3, "🥹": 5})
    summary_json = Column(JSON, nullable=False)

    # OpenAI에게 보낸 prompt (옵션)
    openai_prompt = Column(TEXT, nullable=True)

    # OpenAI의 응답 결과 (옵션)
    response_text = Column(TEXT, nullable=True)
