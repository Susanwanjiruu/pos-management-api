from sqlalchemy import Column, Integer, String, DECIMAL
from database import Base

class Customer(Base):
    __tablename__ = "customers"

    customer_id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False, index=True)
    phone = Column(String(20), nullable=False)
    email = Column(String(100), nullable=False, unique=True, index=True)
    loyalty_points = Column(DECIMAL(10, 2), nullable=False, default=0.00)