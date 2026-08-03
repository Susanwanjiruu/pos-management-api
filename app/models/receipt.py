from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.sql import func
from database import Base

class Receipt(Base):
    __tablename__ = "receipts"

    receipt_id = Column(Integer, primary_key=True, index=True)
    sale = Column(Integer, ForeignKey("sales.sales_id"), nullable=False, unique=True)
    receipt_number = Column(String(50), nullable=False, unique=True, index=True)
    date_issued = Column(DateTime(timezone=True), server_default=func.now())