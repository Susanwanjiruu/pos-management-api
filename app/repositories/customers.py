from sqlalchemy.orm import Session
from app.models.customers import Customer
from app.schemas.customers import CustomerCreate

class CustomerRepository:
    def __init__(self, db: Session):
        self.db = db

    def create_customer(self, customer_data: CustomerCreate):
        db_customer = Customer(**customer_data.model_dump())
        self.db.add(db_customer)
        self.db.commit()
        self.db.refresh(db_customer)
        return db_customer

    def get_by_id(self, customer_id: int):
        return self.db.query(Customer).filter(Customer.customer_id == customer_id).first()

    def get_by_email(self, email: str):
        return self.db.query(Customer).filter(Customer.email == email).first()

    def get_all_customers(self, skip: int = 0, limit: int = 100):
        return self.db.query(Customer).offset(skip).limit(limit).all()

    def update_customer(self, customer_id: int, updated_fields: dict):
        db_customer = self.get_by_id(customer_id)
        if not db_customer:
            return None

        for key, value in updated_fields.items():
            if hasattr(db_customer, key):
                setattr(db_customer, key, value)

        self.db.commit()
        self.db.refresh(db_customer)
        return db_customer

    def delete_customer(self, customer_id: int):
        db_customer = self.get_by_id(customer_id)
        if not db_customer:
            return False

        self.db.delete(db_customer)
        self.db.commit()
        return True