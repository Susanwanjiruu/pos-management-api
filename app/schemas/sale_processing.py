from pydantic import BaseModel, Field
from typing import Optional
from decimal import Decimal
from datetime import datetime

class SaleBase(BaseModel):
    customer: int = Field(..., gt=0)
    product: int = Field(..., gt=0)
    quantity: int = Field(..., gt=0)
    price: Decimal = Field(..., gt=0)
    tax: Decimal = Field(default=0, ge=0)
    discount: Decimal = Field(default=0, ge=0)
    cashier: int = Field(..., gt=0)

class SaleCreate(SaleBase):
    total: Optional[Decimal] = Field(default=None, ge=0)

class SaleResponse(SaleBase):
    sales_id: int
    total: Decimal
    date: datetime

    class Config:
        from_attributes = True