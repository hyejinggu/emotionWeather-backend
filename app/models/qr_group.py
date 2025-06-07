import uuid
from datetime import datetime
from sqlalchemy import Column, TIMESTAMP
from sqlalchemy.dialects.postgresql import UUID
from app.db.base import Base

class QRGroup(Base):
    __tablename__ = "qr_group"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    created_at = Column(TIMESTAMP, nullable=False, default=datetime.utcnow)
    expires_at = Column(TIMESTAMP, nullable=True)
