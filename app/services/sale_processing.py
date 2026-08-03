from sqlalchemy.orm import Session
from fastapi import HTTPException, status
from app.repositories.sale_processing import SaleRepository
from app.repositories.customers import CustomerRepository
from app.repositories.product import ProductRepository
from app.repositories.users import UserRepository
from app.schemas.sale_processing import SaleCreate

class SaleService:
    def __init__(self, db: Session):
        self.repository = SaleRepository(db)
        self.customer_repository = CustomerRepository(db)
        self.product_repository = ProductRepository(db)
        self.user_repository = UserRepository(db)

    def register_new_sale(self, sale_data: SaleCreate):
        customer = self.customer_repository.get_by_id(sale_data.customer)
        if not customer:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"Customer with ID {sale_data.customer} was not found."
            )

        product = self.product_repository.get_by_id(sale_data.product)
        if not product:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"Product with ID {sale_data.product} was not found."
            )

        cashier = self.user_repository.get_by_id(sale_data.cashier)
        if not cashier:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"Cashier (user) with ID {sale_data.cashier} was not found."
            )

        if product.stock_quantity < sale_data.quantity:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=f"Insufficient stock for '{product.product_name}'. "
                       f"Available: {product.stock_quantity}, requested: {sale_data.quantity}."
            )

        total = sale_data.total
        if total is None:
            total = (sale_data.price * sale_data.quantity) - sale_data.discount + sale_data.tax

        sale_fields = sale_data.model_dump(exclude={"total"})
        sale_fields["total"] = total

        new_sale = self.repository.create_sale(sale_fields)

        # Deduct sold quantity from stock
        self.product_repository.update_product(
            product.product_id, {"stock_quantity": product.stock_quantity - sale_data.quantity}
        )

        return new_sale

    def fetch_sale_by_id(self, sales_id: int):
        sale = self.repository.get_by_id(sales_id)
        if not sale:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"Sale with ID {sales_id} was not found."
            )
        return sale

    def fetch_all_sales(self, skip: int = 0, limit: int = 100):
        return self.repository.get_all_sales(skip=skip, limit=limit)