from app.db import Base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship


class Customer(Base):
    __tablename__ = "customers"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    phone = Column(String, unique=True)
    pets = relationship("Pet", secondary="adoptions", back_populates="customers")
