from fastapi import APIRouter, Depends, Form, UploadFile
from sqlalchemy.orm import Session
from app.api.api_depends import get_db
from app.schema import PetCreate, PetCreated, PetSearchResponse
from app.service import save_pet

router = APIRouter()

@router.post("/pets", status_code=201, response_model=PetCreated)
async def create_pet(age: str = Form(), size: str = Form(), type: str = Form(), gender: str = Form(), good_with_children: bool = Form(), photos: list[UploadFile] | None = None, db: Session = Depends(get_db)):
    new_pet = await save_pet(
                    db, 
                    PetCreate(age=age, size=size, type=type, gender=gender, good_with_children=good_with_children), 
                    photos
                )
    return PetCreated(status="success", pet_id=new_pet.id)

@router.get("/pets", response_model=PetSearchResponse)
def search_pets(type: str = "", size: str = "", age: str = "", good_with_children: bool = True, limit: int = 10, skip: int = 0, db: Session = Depends(get_db)):
    pass
