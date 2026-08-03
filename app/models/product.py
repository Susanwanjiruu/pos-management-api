from sqlalchemy import Column,Integer,String,DECIMAL,ForeignKey
from database import Base

class Product(Base):
    __tablename__="products"
    product_id=Column(Integer , primary_key=True, index=True)
    product_name=Column(String(100),nullable=False, index=True)
    category=Column(String(50),nullable=False,index=True)
    selling_price=Column(DECIMAL(10,2),nullable=False)
    cost_price=Column(DECIMAL(10,2),nullable=False)
    stock_quantity=Column(Integer, nullable=False,default=0)
    supplier_id=Column(Integer,ForeignKey("suppliers.supplier_id"),nullable=False)