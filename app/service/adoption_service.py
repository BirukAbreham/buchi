from sqlalchemy.orm import Session
from app.schema import AdoptionCreate
from app.repo import create_adoption, get_pet_by_id, get_customer_by_id


def save_adoption(db: Session, adopt: AdoptionCreate):
    existing_pet = get_pet_by_id(db, adopt.pet_id)
    existing_customer = get_customer_by_id(db, adopt.customer_id)

    if existing_pet and existing_customer:
        return create_adoption(db, adopt)
    else:
        if not existing_pet:
            raise Exception(f"Pet does not exist by given pet id {adopt.pet_id}")
        else:
            raise Exception(
                f"Customer does not exist by given customer id {adopt.customer_id}"
            )
