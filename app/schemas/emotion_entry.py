from pydantic import BaseModel
from typing import Optional
from datetime import datetime
from uuid import UUID

class EmotionEntryCreate(BaseModel): # 모든 Pydantic 스키마는 이 클래스를 상속
    user_session_id: UUID  # 사용자 세션 ID
    emotion: str           # 이모지
    time_type: str         # 'current' 또는 'future'
    timestamp: datetime    # 입력 시각
    
    # Optional[X] = None	있어도 되고 없어도 됨 (nullable=True 역할)
    target_time: Optional[datetime] = None  # 미래 감정이면 설정됨

    
class EmotionEntryRead(EmotionEntryCreate):  # 기존 필드 재사용 (상속)
    id: UUID  # 감정 입력의 고유 ID

    class Config:
        from_attributes = True  # SQLAlchemy 모델을 그대로 Pydantic으로 변환 가능하게 함
