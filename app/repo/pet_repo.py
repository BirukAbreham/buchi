from sqlalchemy.orm import Session
from app.model import Pet, PetPhoto
from app.schema import PetCreate

def create_pet(db: Session, pet: PetCreate):
    pass

def find_pet(db: Session, type: str = "", gender: str = "", size: str = "", age: str = "", good_with_children: bool = True, limit: int = 10, skip: int = 0):
    pass
