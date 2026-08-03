from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from database import get_db
from app.services.supplier import SupplierService
from app.schemas.supplier import SupplierCreate, SupplierResponse
from typing import List

router = APIRouter(prefix="/suppliers", tags=["Supplier Management"])

@router.post("/", response_model=SupplierResponse, status_code=status.HTTP_201_CREATED)
def create_new_supplier_account(supplier_in: SupplierCreate, db: Session = Depends(get_db)):
    service = SupplierService(db)
    return service.register_new_supplier(supplier_in)

@router.get("/{supplier_id}", response_model=SupplierResponse)
def get_single_supplier_details(supplier_id: int, db: Session = Depends(get_db)):
    service = SupplierService(db)
    return service.fetch_supplier_by_id(supplier_id)

@router.get("/", response_model=List[SupplierResponse])
def list_all_registered_suppliers(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    service = SupplierService(db)
    return service.fetch_all_suppliers(skip=skip, limit=limit)
