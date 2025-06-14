from fastapi import APIRouter
from schemas.user import UserCreate, UserUpdate
from crud.user import user_crud


user_router = APIRouter()


@user_router.post("/", status_code=201)
def create_user(user_data: UserCreate):
    return user_crud.create_user(user_data)

@user_router.post("/{user_id}", status_code=200)
def deactivate_user(user_id: int):
    return user_crud.deactivate_user(user_id)

@user_router.get("/{user_id}", status_code=200)
def get_users_by_id(user_id: int):
    return user_crud.get_users_by_id(user_id)

@user_router.patch("/{user_id}", status_code=200)
def update_user(user_id: int, user_data: UserUpdate):
    return user_crud.update_user(user_id, user_data)


@user_router.get("/", status_code=200)
def get_users():
    return user_crud.get_all_users()