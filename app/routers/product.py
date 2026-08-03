from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from database import get_db
from app.services.product import ProductService
from app.schemas.product import ProductCreate, ProductResponse
from typing import List

router = APIRouter(prefix="/products", tags=["Product Management"])

@router.post("/", response_model=ProductResponse, status_code=status.HTTP_201_CREATED)
def create_new_store_product(product_in: ProductCreate, db: Session = Depends(get_db)):
    service = ProductService(db)
    return service.register_new_product(product_in)

@router.get("/{product_id}", response_model=ProductResponse)
def get_single_product_details(product_id: int, db: Session = Depends(get_db)):
    service = ProductService(db)
    return service.fetch_product_by_id(product_id)

@router.get("/", response_model=List[ProductResponse])
def list_all_inventory_items(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    service = ProductService(db)
    return service.fetch_all_inventory(skip=skip, limit=limit)