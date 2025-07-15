from fastapi import APIRouter
from schemas.registration import RegistrationCreate
from services.registration import registration_service

registration_router = APIRouter()

@registration_router.post("/", status_code=201)
def create_registration(registration_data: RegistrationCreate):
    return registration_service.register_user_for_event(registration_data)

@registration_router.get("/", status_code=200)
def get_all_registrations():
    return registration_service.get_all_registrations()

@registration_router.get("/{user_id}/", status_code=200)
def get_user_registrations(user_id: int = None):
    if user_id:
        return registration_service.get_user_registrations(user_id)
    return registration_service.get_all_registrations()


@registration_router.get("/{event_id}/registration", status_code=200)
def get_event_registration(event_id: int):
    return registration_service.get_event_registration(event_id)

@registration_router.patch("/{registration_id}/attendance", status_code=200)
def mark_attendance(registration_id: int):
    return registration_service.mark_attendance(registration_id)

