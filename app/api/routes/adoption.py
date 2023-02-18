from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.api.api_depends import get_db
from app.schema import AdoptionCreate, AdoptionCreated, AdoptListResponse

router = APIRouter()

@router.post("/adoptions", response_model=AdoptionCreated)
def create_adoption(adopt: AdoptionCreate, db: Session = Depends(get_db)):
    pass

@router.get("/adoptions", response_model=AdoptListResponse)
def list_adoptions(from_date: str, to_date: str, limit: int = 10, skip: int = 0, db: Session = Depends(get_db)):
    pass

@router.get("/generateReport")
def generate_report(from_date: str, to_date: str, db: Session = Depends(get_db)):
    pass
