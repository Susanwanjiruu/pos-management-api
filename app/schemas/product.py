from pydantic import BaseModel,Field
from typing import Optional
from decimal import Decimal

class ProductBase(BaseModel):
    product_name: str = Field(..., min_length=2, max_length=100)
    category: str = Field(..., min_length=2, max_length=50)
    supplier_id: int = Field(..., gt=0)
    selling_price: Decimal = Field(..., gt=0)
    cost_price: Decimal = Field(..., gt=0)
    stock_quantity: int = Field(default=0, ge=0)

class ProductCreate(ProductBase):
    pass
class ProductResponse(ProductBase):
    product_id:int

    class Config:
        from_attributes=True
   