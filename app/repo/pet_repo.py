from sqlalchemy.orm import Session
from app.model import Pet, PetPhoto
from app.schema import PetCreate, PetPhotoCreate


def create_pet(db: Session, pet: PetCreate):
    new_pet = Pet(
        age=pet.age,
        size=pet.size,
        type=pet.type,
        gender=pet.gender,
        good_with_children=pet.good_with_children,
    )
    db.add(new_pet)
    db.commit()
    db.refresh(new_pet)
    return new_pet


def create_pet_photo(db: Session, pet_photo: PetPhotoCreate):
    new_photo = PetPhoto(pet_id=pet_photo.pet_id, photo_url=pet_photo.photo_url)
    db.add(new_photo)
    db.commit()
    db.refresh(new_photo)
    return new_photo


def find_pet(
    db: Session,
    type: str = "",
    gender: str = "",
    size: str = "",
    age: str = "",
    good_with_children: bool = True,
    limit: int = 10,
    skip: int = 0,
):
    pass


def get_pet_by_id(db: Session, pet_id: int):
    return db.query(Pet).filter(Pet.id == pet_id).first()
