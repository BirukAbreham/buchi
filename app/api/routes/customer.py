from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.api.api_depends import get_db
from app.schema import CustomerCreate, CustomerCreated
from app.service import save_customer

router = APIRouter()

@router.post("/customers", response_model=CustomerCreated, status_code=201)
def create_customer(customer: CustomerCreate, db: Session = Depends(get_db)):
    new_customer = save_customer(db, customer)
    return CustomerCreated(status="success", customer_id=new_customer.id)
