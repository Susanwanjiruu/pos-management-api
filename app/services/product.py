from sqlalchemy.orm import Session
from fastapi import HTTPException, status
from app.repositories.product import ProductRepository
from app.schemas.product import ProductCreate

class ProductService:
    def __init__(self, db: Session):
  
        self.repository = ProductRepository(db)

    def register_new_product(self, product_data: ProductCreate):
     
        existing_products = self.repository.get_all_products()
        for item in existing_products:
            if item.product_name.lower() == product_data.product_name.lower():
                raise HTTPException(
                    status_code=status.HTTP_400_BAD_REQUEST,
                    detail="A product with this name already exists in inventory."
                )
        
      
        if product_data.selling_price <= product_data.cost_price:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Selling price must be greater than cost price to ensure profitability."
            )

        return self.repository.create_product(product_data)

   
    def fetch_product_by_id(self, product_id: int):
        product = self.repository.get_by_id(product_id)
        if not product:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"Product with ID {product_id} was not found."
            )
        return product

    def fetch_all_inventory(self, skip: int = 0, limit: int = 100):
        return self.repository.get_all_products(skip=skip, limit=limit)

