from fastapi import FastAPI
from database import engine, Base
from app.routers import product, supplier, customers, users, sale_processing, payments, receipts
import app.models.supplier
import app.models.product
import app.models.customers
import app.models.users
import app.models.sale_processing
import app.models.payments
import app.models.receipt


app = FastAPI(
    title="POS Backend System",
    description="An API for tracking Point of Sale operations.",
    version="1.0.0"
)


Base.metadata.create_all(bind=engine)

app.include_router(product.router)
app.include_router(supplier.router)
app.include_router(customers.router)
app.include_router(users.router)
app.include_router(sale_processing.router)
app.include_router(payments.router)
app.include_router(receipts.router)


@app.get("/")
def read_root():
    return "this is a  POS system"
   
