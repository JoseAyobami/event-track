from fastapi import APIRouter
from schemas.event import EventCreate, EventUpdate
from schemas.speaker import SpeakerBase
from crud.event import event_crud


event_router = APIRouter()


@event_router.post("/", status_code=201)
def create_event(event_data: EventCreate):
    return event_crud.create_event(event_data)


@event_router.patch("/{event_id}/close", status_code=200)
def close_event(event_id: int):
    return event_crud.close_events(event_id)

@event_router.get("/{event_id}", status_code=200)
def get_event_by_id(event_id: int):
    return event_crud.get_event_by_id(event_id)

@event_router.patch("/{event_id}", status_code=200)
def update_event(event_id: int, event_data: EventUpdate):
    return event_crud.update_event(event_id, event_data)


@event_router.get("/", status_code=200)
def get_all_events():
    return event_crud.get_all_events()











 
    