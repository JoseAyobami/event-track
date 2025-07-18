from pydantic import BaseModel
from typing import Optional, List 
from datetime import date
from schemas.speaker import SpeakerBase

class EventBase(BaseModel):
    title: str
    location: str


class EventCreate(EventBase):
    is_open: bool = True
    


class EventUpdate(BaseModel):
    title: Optional[str]  = None
    location: Optional[str]  = None
    event_date: Optional[date]  = None  

class Event(EventBase):
    id: int
    event_date: date
    