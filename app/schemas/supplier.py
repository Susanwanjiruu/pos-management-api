from pydantic import BaseModel, Field


class SupplierBase(BaseModel):
    supplier_name: str = Field(..., min_length=2, max_length=100)
    phone: str = Field(..., min_length=5, max_length=20)
    address: str = Field(..., min_length=5, max_length=255)


class SupplierCreate(SupplierBase):
    pass


class SupplierResponse(SupplierBase):
    supplier_id: int

    class Config:
        from_attributes = True
