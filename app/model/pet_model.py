from app.db import Base
from sqlalchemy import Boolean, Column, Integer, String
from sqlalchemy.orm import relationship

class Pet(Base):
    __tablename__ = "pets"

    id = Column(Integer, primary_key=True, index=True)
    age = Column(String)
    size = Column(String)
    type = Column(String)
    gender = Column(String)
    good_with_children = Column(Boolean, default=True)
    customers = relationship("Customer", secondary="adoptions", back_populates="pets")
