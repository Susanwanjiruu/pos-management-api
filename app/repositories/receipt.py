from sqlalchemy.orm import Session
from app.models.receipt import Receipt

class ReceiptRepository:
    def __init__(self, db: Session):
        self.db = db

    def create_receipt(self, sale_id: int, receipt_number: str):
        db_receipt = Receipt(sale=sale_id, receipt_number=receipt_number)
        self.db.add(db_receipt)
        self.db.commit()
        self.db.refresh(db_receipt)
        return db_receipt

    def get_by_id(self, receipt_id: int):
        return self.db.query(Receipt).filter(Receipt.receipt_id == receipt_id).first()

    def get_by_sale(self, sale_id: int):
        return self.db.query(Receipt).filter(Receipt.sale == sale_id).first()

    def get_all_receipts(self, skip: int = 0, limit: int = 100):
        return self.db.query(Receipt).offset(skip).limit(limit).all()