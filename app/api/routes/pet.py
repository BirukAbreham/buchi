from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.api.api_depends import get_db
from app.schema import PetCreate, PetCreated, PetSearchResponse

router = APIRouter()

@router.post("/pets", response_model=PetCreated)
def create_pet(pet: PetCreate, db: Session = Depends(get_db)):
    pass

@router.get("/pets", response_model=PetSearchResponse)
def search_pets(type: str = "", size: str = "", age: str = "", good_with_children: bool = True, limit: int = 10, skip: int = 0, db: Session = Depends(get_db)):
    pass
