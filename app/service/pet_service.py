import aiofiles
import hashlib
import requests
from requests.exceptions import HTTPError
from fastapi import UploadFile
from sqlalchemy.orm import Session
from app.schema import PetCreate, PetPhotoCreate
from app.repo import create_pet, create_pet_photo, get_pets
from app.config import get_settings

settings = get_settings()


def get_unique_filename(filename) -> str:
    photo_name, photo_ext = filename.split(".")[0], filename.split(".")[1]
    unique_filename = (
        hashlib.md5(photo_name.encode("utf-8")).hexdigest() + "." + photo_ext
    )
    return unique_filename


async def save_pet(db: Session, pet: PetCreate, photos: list[UploadFile] | None = None):
    if photos is None or len(photos) == 0:
        new_pet = create_pet(db, pet)
    else:
        new_pet = create_pet(db, pet)

        for photo in photos:
            filename = get_unique_filename(photo.filename)

            async with aiofiles.open(
                settings.UPLOAD_DIR + "/" + filename, "wb"
            ) as file:
                content = await photo.read()
                await file.write(content)

            create_pet_photo(db, PetPhotoCreate(pet_id=new_pet.id, photo_url=filename))

    return new_pet


def get_credentials() -> str:
    url = settings.BASE_URL + "/oauth2/token"
    try:
        response = requests.post(
            url,
            data={
                "grant_type": "client_credentials",
                "client_id": settings.CLIENT_ID,
                "client_secret": settings.CLIENT_SECRET,
            },
        )
        response.raise_for_status()

    except HTTPError as http_error:
        print(f"HTTP error occurred: {http_error}")

    except Exception as error:
        print(f"Other error occurred: {error}")

    else:
        credentials = response.json()
        return credentials["access_token"]


def pet_finder_api_response(access_token: str, params: dict):
    clean_response = []
    url = settings.BASE_URL + "/animals"
    try:
        response = requests.get(
            url, params=params, headers={"Authorization": f"Bearer {access_token}"}
        )
        response.raise_for_status()

    except HTTPError as http_error:
        print(f"HTTP error occurred: {http_error}")

    except Exception as error:
        print(f"Other error occurred: {error}")

    else:
        api_response = response.json()
        for animal in api_response["animals"]:
            photos = []

            for animal_photo in animal["photos"]:
                photos.extend(animal_photo.values())

            clean_response.append(
                {
                    "id": animal["id"],
                    "source": "petfinder",
                    "type": animal["type"],
                    "size": animal["size"],
                    "gender": animal["gender"],
                    "age": animal["age"],
                    "good_with_children": params["good_with_children"],
                    "photos": photos,
                }
            )
        return clean_response


def get_query_params(
    type: list[str] = None,
    size: list[str] = None,
    age: list[str] = None,
    good_with_children: bool = True,
    limit: int = 10,
):
    query_params = {}
    if type is not None:
        query_params["type"] = type

    if size is not None:
        query_params["size"] = size

    if age is not None:
        query_params["age"] = age

    query_params["good_with_children"] = "true" if good_with_children else "false"

    query_params["limit"] = limit

    return query_params


def db_result_formatter(results, url):
    db_result = {}
    for result in results:
        if result[0].id in db_result:
            db_result[result[0].id]["photos"].append(f"{url}/{result[1].photo_url}")
        else:
            db_result[result[0].id] = {
                "id": result[0].id,
                "source": "local",
                "type": result[0].type,
                "size": result[0].size,
                "gender": result[0].gender,
                "age": result[0].age,
                "good_with_children": "true"
                if result[0].good_with_children
                else "false",
                "photos": [f"{url}/{result[1].photo_url}"],
            }

    db_result_ls = []
    for pet_id in db_result.keys():
        db_result_ls.append(db_result[pet_id])

    return db_result_ls


def find_pets(
    db: Session,
    url: str,
    type: list[str] = None,
    size: list[str] = None,
    age: list[str] = None,
    good_with_children: bool = True,
    limit: int = 10,
):
    query_params = get_query_params(
        type=type,
        size=size,
        age=age,
        good_with_children=good_with_children,
        limit=limit,
    )

    # pet finder api result
    access_token = get_credentials()
    api_search_result = None
    if access_token:
        api_search_result = pet_finder_api_response(
            access_token=access_token, params=query_params
        )

    # database results
    db_results = get_pets(db=db, params=query_params)

    com_results = []
    com_results.extend(db_result_formatter(db_results, url))
    if api_search_result:
        com_results.extend(api_search_result)
    return com_results
