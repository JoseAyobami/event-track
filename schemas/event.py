from pydantic import BaseModel
from datetime import date

class EventBase(BaseModel):
    title: str
    location: str


class EventCreate(EventBase):
    is_open: bool = True

class Event(EventBase):
    id: int
    event_date: date 
    