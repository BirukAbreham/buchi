from fastapi import APIRouter, Depends, Form, UploadFile, Query, Request
from sqlalchemy.orm import Session
from app.api.api_depends import get_db
from app.schema import PetCreate, PetCreated, PetSearchResponse
from app.service import save_pet, find_pets

router = APIRouter()


@router.post("/pets", status_code=201, response_model=PetCreated)
async def create_pet(
    age: str = Form(),
    size: str = Form(),
    type: str = Form(),
    gender: str = Form(),
    good_with_children: bool = Form(),
    photos: list[UploadFile] | None = None,
    db: Session = Depends(get_db),
):
    new_pet = await save_pet(
        db,
        PetCreate(
            age=age,
            size=size,
            type=type,
            gender=gender,
            good_with_children=good_with_children,
        ),
        photos,
    )
    return PetCreated(status="success", pet_id=new_pet.id)


@router.get("/pets")
def search_pets(
    request: Request,
    type: list[str] = Query(None),
    size: list[str] = Query(None),
    age: list[str] = Query(None),
    good_with_children: bool = True,
    limit: int = 10,
    db: Session = Depends(get_db),
):
    url_segments = request.url._url.split("/")
    host_url = f"{url_segments[0]}//{url_segments[2]}/pet_photos"
    pets = find_pets(
        db=db,
        url=host_url,
        type=type,
        size=size,
        age=age,
        good_with_children=good_with_children,
        limit=limit,
    )
    return {"status": "success", "pets": pets}
