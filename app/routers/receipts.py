from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from database import get_db
from app.services.receipts import ReceiptService
from app.schemas.receipts import ReceiptCreate, ReceiptResponse
from typing import List

router = APIRouter(prefix="/receipts", tags=["Receipt Generation"])

@router.post("/", response_model=ReceiptResponse, status_code=status.HTTP_201_CREATED)
def issue_new_receipt(receipt_in: ReceiptCreate, db: Session = Depends(get_db)):
    service = ReceiptService(db)
    return service.register_new_receipt(receipt_in)

@router.get("/{receipt_id}", response_model=ReceiptResponse)
def get_single_receipt_details(receipt_id: int, db: Session = Depends(get_db)):
    service = ReceiptService(db)
    return service.fetch_receipt_by_id(receipt_id)

@router.get("/", response_model=List[ReceiptResponse])
def list_all_receipts(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    service = ReceiptService(db)
    return service.fetch_all_receipts(skip=skip, limit=limit)