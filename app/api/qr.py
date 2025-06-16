from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

import qrcode
import io
import base64

from app.db.session import get_db
from app.models.qr_group import QRGroup
from app.schemas.qr_group import QRResponse

router = APIRouter()

@router.post("/qr/create-group", response_model=QRResponse)
async def create_qr_group(db: AsyncSession = Depends(get_db)):
    # 1. QR Group 생성 및 저장
    new_group = QRGroup()
    db.add(new_group)
    await db.commit()
    await db.refresh(new_group)

    # 2. URL 및 QR 생성
    session_url = f"http://localhost:8000/session/{new_group.id}"  # 나중에 실제 도메인으로 변경
    qr = qrcode.make(session_url)
    buf = io.BytesIO()
    qr.save(buf, format="PNG")
    qr_base64 = base64.b64encode(buf.getvalue()).decode("utf-8")

    return {
        "qr_group_id": str(new_group.id),
        "session_url": session_url,
        "qr_image_base64": qr_base64,
    }
