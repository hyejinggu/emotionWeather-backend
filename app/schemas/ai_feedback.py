from pydantic import BaseModel
from typing import List, Literal, Dict


class EmotionForecast(BaseModel):
    label: Literal["현재", "가까운 미래", "조금 더 먼 미래"]
    time: str
    forecast: str
    warnings: str
    supporting_msg: str


class AIFeedback(BaseModel):
    overall_summary: str
    time_segments: List[EmotionForecast]
    commentary: str


class EmotionSummaryResponse(BaseModel):
    summary: Dict[str, Dict[str, int]]
    feedback: AIFeedback
