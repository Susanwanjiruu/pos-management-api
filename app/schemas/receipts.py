from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime

class ReceiptBase(BaseModel):
    sale: int = Field(..., gt=0)

class ReceiptCreate(ReceiptBase):
    receipt_number: Optional[str] = Field(default=None, max_length=50)

class ReceiptResponse(ReceiptBase):
    receipt_id: int
    receipt_number: str
    date_issued: datetime

    class Config:
        from_attributes = True