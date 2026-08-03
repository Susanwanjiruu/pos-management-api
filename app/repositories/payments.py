from sqlalchemy.orm import Session
from app.models.payments import Payment
from app.schemas.payments import PaymentCreate

class PaymentRepository:
    def __init__(self, db: Session):
        self.db = db

    def create_payment(self, payment_data: PaymentCreate):
        db_payment = Payment(**payment_data.model_dump())
        self.db.add(db_payment)
        self.db.commit()
        self.db.refresh(db_payment)
        return db_payment

    def get_by_id(self, payment_id: int):
        return self.db.query(Payment).filter(Payment.payment_id == payment_id).first()

    def get_all_payments(self, skip: int = 0, limit: int = 100):
        return self.db.query(Payment).offset(skip).limit(limit).all()

    def get_by_sale(self, sale_id: int):
        return self.db.query(Payment).filter(Payment.sale == sale_id).all()