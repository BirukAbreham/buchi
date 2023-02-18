from sqlalchemy.orm import Session
from app.model import Customer
from app.schema import CustomerCreate

def create_customer(db: Session, customer: CustomerCreate):
    new_customer = Customer(name=customer.name, phone=customer.phone)
    db.add(new_customer)
    db.commit()
    db.refresh(new_customer)
    return new_customer

def get_customer_by_phone(db: Session, phone: str):
    return db.query(Customer).filter(Customer.phone == phone).first()
