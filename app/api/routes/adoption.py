from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.api.api_depends import get_db
from app.schema import AdoptionCreate, AdoptionCreated, AdoptListResponse
from app.service import save_adoption

router = APIRouter()

@router.post("/adoptions", response_model=AdoptionCreated, status_code=201)
def create_adoption(adopt: AdoptionCreate, db: Session = Depends(get_db)):
    try:
        new_adoption = save_adoption(db, adopt)
        return AdoptionCreated(status="success", adoption_id=new_adoption.id)
    except:
        raise HTTPException(status_code=422, detail="Customer or Pet does not exist by the given id")

@router.get("/adoptions", response_model=AdoptListResponse)
def list_adoptions(from_date: str, to_date: str, limit: int = 10, skip: int = 0, db: Session = Depends(get_db)):
    pass

@router.get("/generateReport")
def generate_report(from_date: str, to_date: str, db: Session = Depends(get_db)):
    pass
