from app.db import engine
from app.api.router import api_router
from app.model import Adopt, Customer, Pet, PetPhoto
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware, 
    allow_origin=["*"], 
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

Pet.metadata.create_all(bind=engine)
PetPhoto.metadata.create_all(bind=engine)
Customer.metadata.create_all(bind=engine)
Adopt.metadata.create_all(bind=engine)

app.include_router(api_router)
