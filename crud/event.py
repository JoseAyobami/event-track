from fastapi import HTTPException
from schemas.event import EventCreate, EventUpdate
from database import events, speakers
from models import Event as EventModel
from datetime import date


class EventCrud:

    @staticmethod
    def create_event(event_data: EventCreate):
        for speaker in speakers:
            if speaker.id == event_data.speaker_id:
                break
        else:
            raise HTTPException(
                status_code=404, 
                detail="Speaker not found"
            )
        
        event_id = len(events) + 1
        event = EventModel(id=event_id, event_date=date.today(), **event_data.model_dump())
        events.append(event)
        return event
    
       
    
    @staticmethod
    def get_event_by_id(event_id: int):
        for event in events:
            if event.id == event_id:
                return event
        raise HTTPException(
            status_code=404, 
            detail="Event not found")  
    
    @staticmethod
    def update_event(event_id: int, event_data: EventUpdate):
        for event in events:
            if event.id == event_id:
                if event_data.title:
                    event.title = event_data.title
                if event_data.location:
                    event.location = event_data.location
                if event_data.event_date:
                    event.event_date = event_data.event_date
                return event
        raise HTTPException(
            status_code=404, 
            detail="Event not found")                

                

    
    @staticmethod
    def close_events(event_id: int):
        for event in events:
            if event.id == event_id:
                if not event.is_open:
                    raise HTTPException(status_code=403, detail="Event is not open")
                event.is_open = False
                return {"messgae": "Event closed successfully"}
        raise HTTPException(
            status_code=404, 
            detail="Event not found"
        )    

    @staticmethod
    def get_all_events():
        return events


event_crud = EventCrud()      
