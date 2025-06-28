import uuid
from datetime import datetime
from sqlalchemy import Column, TIMESTAMP, Text, String
from sqlalchemy.dialects.postgresql import UUID
from app.db.base import Base

class QRGroup(Base):
    __tablename__ = "qr_group"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    created_at = Column(TIMESTAMP, nullable=False, default=datetime.utcnow)
    expires_at = Column(TIMESTAMP, nullable=True)
    group_name = Column(String(100), nullable=True)  # 그룹 이름
    qr_image = Column(Text, nullable=True)           # QR 이미지 (Base64)