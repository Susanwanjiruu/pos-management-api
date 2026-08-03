from sqlalchemy import Column, Integer, String, DECIMAL, DateTime, ForeignKey
from sqlalchemy.sql import func
from database import Base

class Sale(Base):
    __tablename__ = "sales"

    sales_id = Column(Integer, primary_key=True, index=True)
    customer = Column(Integer, ForeignKey("customers.customer_id"), nullable=False)
    product = Column(Integer, ForeignKey("products.product_id"), nullable=False)
    date = Column(DateTime(timezone=True), server_default=func.now())
    quantity = Column(Integer, nullable=False)
    price = Column(DECIMAL(10, 2), nullable=False)
    tax = Column(DECIMAL(10, 2), nullable=False, default=0)
    discount = Column(DECIMAL(10, 2), nullable=False, default=0)
    total = Column(DECIMAL(10, 2), nullable=False)
    cashier = Column(Integer, ForeignKey("users.user_id"), nullable=False)