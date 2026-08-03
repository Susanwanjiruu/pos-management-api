from sqlalchemy import Column, Integer, String
from database import Base

class Supplier(Base):
    __tablename__ = "suppliers"

    supplier_id = Column(Integer, primary_key=True, index=True)
    supplier_name = Column(String(100), nullable=False, index=True)
    phone = Column(String(20), nullable=False)
    address = Column(String(255), nullable=False)
