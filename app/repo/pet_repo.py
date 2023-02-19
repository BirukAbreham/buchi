from sqlalchemy import and_
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


def get_pets(db: Session, params: dict):
    filter_ls = []

    print("get_pets: ", params)

    if "type" in params:
        filter_ls.append(Pet.type.in_(params["type"]))

    if "size" in params:
        filter_ls.append(Pet.size.in_(params["size"]))

    if "age" in params:
        filter_ls.append(Pet.age.in_(params["age"]))

    if "good_with_children" in params:
        filter_ls.append(Pet.good_with_children == params["good_with_children"])

    return (
        db.query(Pet, PetPhoto)
        .join(PetPhoto, and_(PetPhoto.pet_id == Pet.id))
        .filter(*filter_ls)
        .limit(params["limit"])
        .all()
    )


def get_pet_by_id(db: Session, pet_id: int):
    return db.query(Pet).filter(Pet.id == pet_id).first()
