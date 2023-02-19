import aiofiles
import hashlib
from fastapi import UploadFile
from sqlalchemy.orm import Session
from app.schema import PetCreate, PetPhotoCreate
from app.repo import create_pet, create_pet_photo
from app.config import get_settings

settings = get_settings()


def get_unique_filename(filename) -> str:
    photo_name, photo_ext = filename.split(".")[0], filename.split(".")[1]

    unique_filename = (
        hashlib.md5(photo_name.encode("utf-8")).hexdigest() + "." + photo_ext
    )

    return unique_filename


async def save_pet(db: Session, pet: PetCreate, photos: list[UploadFile] | None = None):
    if photos is None or len(photos) == 0:
        new_pet = create_pet(db, pet)
    else:
        new_pet = create_pet(db, pet)

        for photo in photos:
            filename = get_unique_filename(photo.filename)

            async with aiofiles.open(
                settings.UPLOAD_DIR + "/" + filename, "wb"
            ) as file:
                content = await photo.read()
                await file.write(content)

            create_pet_photo(db, PetPhotoCreate(pet_id=new_pet.id, photo_url=filename))

    return new_pet
