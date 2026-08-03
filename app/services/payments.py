from sqlalchemy.orm import Session
from fastapi import HTTPException, status
from app.repositories.payments import PaymentRepository
from app.repositories.sale_processing import SaleRepository
from app.schemas.payments import PaymentCreate

class PaymentService:
    def __init__(self, db: Session):
        self.repository = PaymentRepository(db)
        self.sale_repository = SaleRepository(db)

    def register_new_payment(self, payment_data: PaymentCreate):
        sale = self.sale_repository.get_by_id(payment_data.sale)
        if not sale:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"Sale with ID {payment_data.sale} was not found."
            )
        return self.repository.create_payment(payment_data)

    def fetch_payment_by_id(self, payment_id: int):
        payment = self.repository.get_by_id(payment_id)
        if not payment:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"Payment with ID {payment_id} was not found."
            )
        return payment

    def fetch_all_payments(self, skip: int = 0, limit: int = 100):
        return self.repository.get_all_payments(skip=skip, limit=limit)