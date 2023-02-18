from sqlalchemy.orm import Session
from app.schema import CustomerCreate
from app.repo import create_customer, get_customer_by_phone

def save_customer(db: Session, customer: CustomerCreate):
    existing_customer = get_customer_by_phone(db, customer.phone)

    if existing_customer:
        return existing_customer
    else:
        return create_customer(db, customer)    
