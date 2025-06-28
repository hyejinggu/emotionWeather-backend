from pydantic import BaseModel

class QRResponse(BaseModel):
    qr_group_id: str
    qr_group_name: str
    session_url: str
    qr_image_base64: str
    