from pydantic import BaseModel
from app.schema.customer_schema import CustomerSchema
from app.schema.pet_schema import PetSchema


class AdoptResponseBase(BaseModel):
    status: str


class AdoptionCreate(BaseModel):
    pet_id: int
    customer_id: int


class AdoptionCreated(AdoptResponseBase):
    adoption_id: int


class AdoptSchema(BaseModel):
    pet_id: int
    customer_id: int
    pet: PetSchema
    customer: CustomerSchema

    class Config:
        orm_mode = True


class AdoptListResponse(AdoptResponseBase):
    data: list[AdoptSchema] = []
