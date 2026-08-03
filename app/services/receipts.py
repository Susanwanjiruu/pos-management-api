import uuid

from sqlalchemy.orm import Session
from fastapi import HTTPException, status
from app.repositories.receipt import ReceiptRepository
from app.repositories.sale_processing import SaleRepository
from app.schemas.receipts import ReceiptCreate

class ReceiptService:
    def __init__(self, db: Session):
        self.repository = ReceiptRepository(db)
        self.sale_repository = SaleRepository(db)

    def register_new_receipt(self, receipt_data: ReceiptCreate):
        sale = self.sale_repository.get_by_id(receipt_data.sale)
        if not sale:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"Sale with ID {receipt_data.sale} was not found."
            )

        if self.repository.get_by_sale(receipt_data.sale):
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=f"A receipt already exists for sale {receipt_data.sale}."
            )

        receipt_number = receipt_data.receipt_number or f"RCPT-{uuid.uuid4().hex[:10].upper()}"
        return self.repository.create_receipt(receipt_data.sale, receipt_number)

    def fetch_receipt_by_id(self, receipt_id: int):
        receipt = self.repository.get_by_id(receipt_id)
        if not receipt:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"Receipt with ID {receipt_id} was not found."
            )
        return receipt

    def fetch_all_receipts(self, skip: int = 0, limit: int = 100):
        return self.repository.get_all_receipts(skip=skip, limit=limit)