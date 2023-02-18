from app.db import Base
from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship

class Adopt(Base):
    __tablename__ = "adoptions"
    
    pet_id = Column(Integer, ForeignKey("pets.id"), primary_key=True)
    customer_id = Column(Integer, ForeignKey("customers.id"), primary_key=True)

    pets = relationship("Pet", back_populates="customers")
    customers = relationship("Customer", back_populates="pets")
