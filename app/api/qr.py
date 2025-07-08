from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select, update

import qrcode, base64, uuid, io

from app.db.session import get_db
from app.models.qr_group import QRGroup
from app.schemas.qr_group import QRResponse, UpdateQRGroupNameRequest

router = APIRouter()

SESSION_BASE_URL = "http://localhost:8000/session"

@router.post("/qr/create-group", response_model=QRResponse)
async def create_qr_group(db: AsyncSession = Depends(get_db)):
     # 1. UUID 직접 생성
    group_id = uuid.uuid4()

    # 2. URL 및 QR 생성 (고정된 UUID 사용)
    session_url = f"{SESSION_BASE_URL}/{group_id}"
    qr = qrcode.make(session_url)
    buf = io.BytesIO()
    qr.save(buf, format="PNG")
    qr_base64 = base64.b64encode(buf.getvalue()).decode("utf-8")

    # 3. QRGroup 객체 생성 (UUID 수동 지정)
    new_group = QRGroup(
        id=group_id,
        group_name="groupname",
        qr_image=qr_base64,
    )
    db.add(new_group)
    await db.commit()
    await db.refresh(new_group)

    return {
        "qr_group_id": str(new_group.id),
        "qr_group_name": str(new_group.group_name),
        "session_url": session_url,
        "qr_image_base64": qr_base64,
    }
    

@router.get("/qr/group-info", response_model=QRResponse)
async def get_group_info(groupId: str, db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(QRGroup).where(QRGroup.id == groupId))
    group = result.scalar_one_or_none()
    
    if not group:
        raise HTTPException(status_code=404, detail="Group not found")

    return {
        "qr_group_id": str(group.id),
        "qr_group_name": str(group.group_name),
        "session_url": f"{SESSION_BASE_URL}/{group.id}",
        "qr_image_base64": str(group.qr_image),
    }
    

@router.put("qr/group-name")
async def modify_group_name(
    payload: UpdateQRGroupNameRequest,
    db: AsyncSession = Depends(get_db)
):
    result = await db.execute(
        update(QRGroup)
        .where(QRGroup.id == payload.qr_group_id)
        .values(group_name=payload.group_name)
        .returning(QRGroup.group_name)
    )
    await db.commit()

    updated_name = result.scalar()
    if not updated_name:
        raise HTTPException(status_code=404, detail="QR 그룹을 찾을 수 없습니다.")

    return {
        "updated_group_name": updated_name
    }
