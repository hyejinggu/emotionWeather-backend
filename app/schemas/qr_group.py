from pydantic import BaseModel

class QRResponse(BaseModel):
    qr_group_id: str
    session_url: str
    qr_image_base64: str