from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from database import get_db
from app.services.payments import PaymentService
from app.schemas.payments import PaymentCreate, PaymentResponse
from typing import List

router = APIRouter(prefix="/payments", tags=["Payment Handling"])

@router.post("/", response_model=PaymentResponse, status_code=status.HTTP_201_CREATED)
def record_new_payment(payment_in: PaymentCreate, db: Session = Depends(get_db)):
    service = PaymentService(db)
    return service.register_new_payment(payment_in)

@router.get("/{payment_id}", response_model=PaymentResponse)
def get_single_payment_details(payment_id: int, db: Session = Depends(get_db)):
    service = PaymentService(db)
    return service.fetch_payment_by_id(payment_id)

@router.get("/", response_model=List[PaymentResponse])
def list_all_payments(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    service = PaymentService(db)
    return service.fetch_all_payments(skip=skip, limit=limit)