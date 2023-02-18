from sqlalchemy.orm import Session
from app.model import Customer
from app.schema import CustomerCreate

def create_customer(db: Session, customer: CustomerCreate):
    pass
