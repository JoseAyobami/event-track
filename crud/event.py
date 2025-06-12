from schemas.event import EventCreate
from database import events
from models import Event as EventModel
from datetime import date


class EventCrud:

    @staticmethod
    def create_event(event_data: EventCreate):
        event_id = len(events) + 1
        event = EventModel(id=event_id, event_date=date.today(), **event_data.model_dump())
        events.append(event)
        return event
    
    @staticmethod
    def get_event_by_id(event_id: int):
        for event in events:
            if event.id == event_id:
                return event
        return {"message": "Event not exist"}  
    
    @staticmethod
    def close_events(event_id: int):
        for event in events:
            if event.id == event_id:
                event.is_open = False
                if not event.is_open:
                    break
                return {"messgae": "Event closed sucessfully"}
        return {"meesage": "Event not found or event deleted successfully"}

    @staticmethod
    def get_all_events():
        return events


event_crud = EventCrud()      
