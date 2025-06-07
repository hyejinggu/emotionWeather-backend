import uuid
from datetime import datetime
from sqlalchemy import Column, TIMESTAMP
from sqlalchemy.dialects.postgresql import UUID
from app.db.base import Base

class UserSession(Base):
    __tablename__ = "user_session"  # 실제 DB 테이블 이름

    # UUID: 고유 식별자. 기본값으로 uuid.uuid4()를 설정하면 자동 생성됨
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)

    # 연결된 QR 그룹의 ID. 외래 키는 아니지만 UUID 형식으로 저장
    # as_uuid=True는 Python에서도 UUID 객체로 다루겠다는 의미
    qr_group_id = Column(UUID(as_uuid=True), nullable=False)

    # 접속한 시간. 기본값은 현재 시간
    joined_at = Column(TIMESTAMP, nullable=False, default=datetime.utcnow)