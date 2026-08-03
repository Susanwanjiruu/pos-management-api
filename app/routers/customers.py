from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from database import get_db
from app.services.customers import CustomerService
from app.schemas.customers import CustomerCreate, CustomerResponse
from typing import List

router = APIRouter(prefix="/customers", tags=["Customer Management"])

@router.post("/", response_model=CustomerResponse, status_code=status.HTTP_201_CREATED)
def register_new_customer(customer_in: CustomerCreate, db: Session = Depends(get_db)):
    service = CustomerService(db)
    return service.register_new_customer(customer_in)

@router.get("/{customer_id}", response_model=CustomerResponse)
def get_single_customer_details(customer_id: int, db: Session = Depends(get_db)):
    service = CustomerService(db)
    return service.fetch_customer_by_id(customer_id)

@router.get("/", response_model=List[CustomerResponse])
def list_all_customers(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    service = CustomerService(db)
    return service.fetch_all_customers(skip=skip, limit=limit)

@router.delete("/{customer_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_customer(customer_id: int, db: Session = Depends(get_db)):
    service = CustomerService(db)
    service.remove_customer(customer_id)