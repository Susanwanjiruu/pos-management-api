from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from database import get_db
from app.services.sale_processing import SaleService
from app.schemas.sale_processing import SaleCreate, SaleResponse
from typing import List

router = APIRouter(prefix="/sales", tags=["Sales Processing"])

@router.post("/", response_model=SaleResponse, status_code=status.HTTP_201_CREATED)
def process_new_sale(sale_in: SaleCreate, db: Session = Depends(get_db)):
    service = SaleService(db)
    return service.register_new_sale(sale_in)

@router.get("/{sales_id}", response_model=SaleResponse)
def get_single_sale_details(sales_id: int, db: Session = Depends(get_db)):
    service = SaleService(db)
    return service.fetch_sale_by_id(sales_id)

@router.get("/", response_model=List[SaleResponse])
def list_all_sales(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    service = SaleService(db)
    return service.fetch_all_sales(skip=skip, limit=limit)