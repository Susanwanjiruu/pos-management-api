from sqlalchemy import Column, Integer, String, DECIMAL, DateTime, ForeignKey
from sqlalchemy.sql import func
from database import Base

class Payment(Base):
    __tablename__ = "payments"

    payment_id = Column(Integer, primary_key=True, index=True)
    sale = Column(Integer, ForeignKey("sales.sales_id"), nullable=False)
    payment_method = Column(String(30), nullable=False)
    amount = Column(DECIMAL(10, 2), nullable=False)
    date = Column(DateTime(timezone=True), server_default=func.now())