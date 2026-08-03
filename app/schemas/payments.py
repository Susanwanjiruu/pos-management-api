from pydantic import BaseModel, Field
from typing import Literal
from decimal import Decimal
from datetime import datetime

class PaymentBase(BaseModel):
    sale: int = Field(..., gt=0)
    payment_method: Literal["cash", "card", "mobile money"]
    amount: Decimal = Field(..., gt=0)

class PaymentCreate(PaymentBase):
    pass

class PaymentResponse(PaymentBase):
    payment_id: int
    date: datetime

    class Config:
        from_attributes = True