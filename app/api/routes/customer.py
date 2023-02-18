from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.api.api_depends import get_db
from app.schema import CustomerCreate, CustomerCreated

router = APIRouter()

@router.post("/customers", response_model=CustomerCreated)
def create_customer(customer: CustomerCreate, db: Session = Depends(get_db)):
    pass
