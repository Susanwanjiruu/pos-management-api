from pydantic import BaseModel, Field
from decimal import Decimal

class CustomerBase(BaseModel):
    name: str = Field(..., min_length=2, max_length=100)
    phone: str = Field(..., min_length=5, max_length=20)
    email: str = Field(..., min_length=5, max_length=100)
    loyalty_points: Decimal = Field(default=Decimal("0.00"), ge=0)

class CustomerCreate(CustomerBase):
    pass

class CustomerResponse(CustomerBase):
    customer_id: int

    class Config:
        from_attributes = True