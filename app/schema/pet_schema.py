from pydantic import BaseModel

class PetResponseBase(BaseModel):
    status: str

class PetCreate(BaseModel):
    age: str
    size: str
    type: str
    gender: str
    good_with_children: bool

class PetCreated(PetResponseBase):
    pet_id: int

class PhotoSchema(BaseModel):
    photo_url: str

    class Config:
        orm_mode = True

class PetSchema(BaseModel):
    id: int
    source: str
    type: str
    gender: str
    size: str
    age: str
    good_with_children: bool
    photos: list[PhotoSchema] = []

    class Config:
        orm_mode = True

class PetSearchResponse(PetResponseBase):
    pets: list[PetSchema] = []
