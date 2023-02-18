from fastapi import APIRouter
from app.api.routes import adoption, customer, pet

api_router = APIRouter()

api_router.include_router(pet.router, tags=["pets"])
api_router.include_router(customer.router, tags=["customer"])
api_router.include_router(adoption.router, tags=["adoption"])
