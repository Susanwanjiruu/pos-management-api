from sqlalchemy.orm import Session
from app.models.sale_processing import Sale

class SaleRepository:
    def __init__(self, db: Session):
        self.db = db

    def create_sale(self, sale_fields: dict):
        db_sale = Sale(**sale_fields)
        self.db.add(db_sale)
        self.db.commit()
        self.db.refresh(db_sale)
        return db_sale

    def get_by_id(self, sales_id: int):
        return self.db.query(Sale).filter(Sale.sales_id == sales_id).first()

    def get_all_sales(self, skip: int = 0, limit: int = 100):
        return self.db.query(Sale).offset(skip).limit(limit).all()

    def delete_sale(self, sales_id: int):
        db_sale = self.get_by_id(sales_id)
        if not db_sale:
            return False

        self.db.delete(db_sale)
        self.db.commit()
        return True