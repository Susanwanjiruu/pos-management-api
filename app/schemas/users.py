from pydantic import BaseModel, Field
from typing import Literal

class UserBase(BaseModel):
    username: str = Field(..., min_length=3, max_length=50)
    full_name: str = Field(..., min_length=2, max_length=100)
    role: Literal["cashier", "manager", "admin"]

class UserCreate(UserBase):
    password: str = Field(..., min_length=6, max_length=100)

class UserResponse(UserBase):
    user_id: int

    class Config:
        from_attributes = True

class UserLogin(BaseModel):
    username: str
    password: str