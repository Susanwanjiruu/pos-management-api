from sqlalchemy.orm import Session
from app.models.supplier import Supplier
from app.schemas.supplier import SupplierCreate

class SupplierRepository:
    def __init__(self, db: Session):

        self.db = db

    def create_supplier(self, supplier_data: SupplierCreate):
        db_supplier = Supplier(**supplier_data.model_dump())
        self.db.add(db_supplier)
        self.db.commit()
        self.db.refresh(db_supplier)
        return db_supplier


    def get_by_id(self, supplier_id: int):
        return self.db.query(Supplier).filter(Supplier.supplier_id == supplier_id).first()

    def get_all_suppliers(self, skip: int = 0, limit: int = 100):
        return self.db.query(Supplier).offset(skip).limit(limit).all()


    def update_supplier(self, supplier_id: int, updated_fields: dict):
        db_supplier = self.get_by_id(supplier_id)
        if not db_supplier:
            return None
            
        for key, value in updated_fields.items():
            if hasattr(db_supplier, key):
                setattr(db_supplier, key, value)
                
        self.db.commit()
        self.db.refresh(db_supplier)
        return db_supplier


    def delete_supplier(self, supplier_id: int):
        db_supplier = self.get_by_id(supplier_id)
        if not db_supplier:
            return False
            
        self.db.delete(db_supplier)
        self.db.commit()
        return True
