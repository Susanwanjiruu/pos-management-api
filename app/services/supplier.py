from sqlalchemy.orm import Session
from fastapi import HTTPException, status
from app.repositories.supplier import SupplierRepository
from app.schemas.supplier import SupplierCreate

class SupplierService:
    def __init__(self, db: Session):

        self.repository = SupplierRepository(db)

    def register_new_supplier(self, supplier_data: SupplierCreate):
        existing_suppliers = self.repository.get_all_suppliers()
        for vendor in existing_suppliers:
            if vendor.supplier_name.lower() == supplier_data.supplier_name.lower():
                raise HTTPException(
                    status_code=status.HTTP_400_BAD_REQUEST,
                    detail="A supplier company with this exact name is already registered."
                )
        return self.repository.create_supplier(supplier_data)

    def fetch_supplier_by_id(self, supplier_id: int):
        supplier = self.repository.get_by_id(supplier_id)
        if not supplier:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"Supplier account with ID {supplier_id} was not found."
            )
        return supplier

    def fetch_all_suppliers(self, skip: int = 0, limit: int = 100):
        return self.repository.get_all_suppliers(skip=skip, limit=limit)


    def modify_supplier(self, supplier_id: int, updated_fields: dict):

        self.fetch_supplier_by_id(supplier_id)
        return self.repository.update_supplier(supplier_id, updated_fields)

    def remove_supplier(self, supplier_id: int):
        self.fetch_supplier_by_id(supplier_id)
        return self.repository.delete_supplier(supplier_id)
