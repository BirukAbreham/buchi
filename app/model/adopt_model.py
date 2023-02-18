from app.db import Base
from sqlalchemy import Column, Integer, ForeignKey

class Adopt(Base):
    __tablename__ = "adoptions"

    pet_id = Column(Integer, ForeignKey("pets.id"), primary_key=True)
    customer_id = Column(Integer, ForeignKey("customers.id"), primary_key=True)
