from sqlalchemy.orm import Session
from app.model import Adopt
from app.schema import AdoptionCreate

def create_adoption(db: Session, adopt: AdoptionCreate):
    pass

def find_adoptions(db: Session, from_date: str, to_date: str, limit: int = 10, skip: int = 0):
    pass

def generate_report(db: Session, from_date: str, to_date: str):
    pass
