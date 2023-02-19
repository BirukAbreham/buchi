from pydantic import BaseModel


class CustomerResponseBase(BaseModel):
    status: str


class CustomerCreate(BaseModel):
    name: str
    phone: str


class CustomerCreated(CustomerResponseBase):
    customer_id: int


class CustomerSchema(BaseModel):
    id: int
    name: str
    phone: str

    class Config:
        orm_mode = True
