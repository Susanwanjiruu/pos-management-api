from sqlalchemy.orm import Session
from app.models.product import Product
from app.schemas.product import ProductCreate

class ProductRepository:
    def __init__(self,db:Session):
        self.db=db

    def create_product(self,product_data:ProductCreate):
        db_product=Product(**product_data.model_dump())

        self.db.add(db_product)
        self.db.commit()
        self.db.refresh(db_product)  
        return db_product
    def get_by_id(self,product_id:int):
        return self.db.query(Product).filter(Product.product_id==product_id).first()

    def get_all_products(self,skip:int=0, limit:int = 100):
        return self.db.query(Product).offset(skip).limit(limit).all()

    def update_product(self,product_id:int,update_fields: dict):
        db_product=self.get_by_id(product_id)
        if not db_product:
            return "Does not exist"

        for key,value in update_fields.items():
            if hasattr(db_product,key):
                setattr(db_product,key,value)

        self.db.add(db_product)
        self.db.commit()
        self.db.refresh(db_product)  
        return db_product

    def delete_product(self,product_id: int):
        db_product = self.get_by_id(product_id)
        if not db_product:
            return False

        self.db.delete(db_product)
        self.db.commit()
        return True