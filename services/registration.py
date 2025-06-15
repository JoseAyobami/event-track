from fastapi import HTTPException
from database import users, events
from crud.user import user_crud
from crud.event import event_crud
from crud.register import register_crud
from schemas.registration import RegistrationCreate

class RegistrationService:

    @staticmethod
    def register_user_for_event(registration_data: RegistrationCreate):
        user = user_crud.get_users_by_id(registration_data.user_id)
        for user in users:
            if not user:
                raise HTTPException(status_code=404, detail="User not found")
            
            if not user.is_active:
                raise HTTPException(status_code=400, detail="User not active")
            
            if register_crud.is_user_registered(registration_data.event_id, registration_data.user_id):
                raise HTTPException(status_code=400, detail="User is already registered for this event")

           

        
        event = event_crud.get_event_by_id(registration_data.event_id)
        for event in events:
            if not event:
                raise HTTPException(status_code=404, detail="Event not found")
            
            if not event.is_open:
                raise HTTPException(status_code=404, detail="Event not open")                               
        
          
        reg = register_crud.create_event_registration(registration_data) 
        return {"message": f"User registered for event {event.title} successfully", "registration": reg}


    @staticmethod
    def mark_attendance(event_id: int, user_id: int):
        registration = register_crud.mark_attendance(event_id, user_id)
        if not registration:
            raise HTTPException(
                status_code=404,
                detail="Registration not found"
            )
        return {
            "message": "Attendance marked successfully",
            "registration": registration
        }

    
    @staticmethod
    def get_user_registrations(user_id: int):
        return register_crud.get_registration_user_id(user_id)
    
    @staticmethod
    def get_event_registration(event_id: int):
        return register_crud.get_event_registration(event_id)

    
    @staticmethod
    def get_all_registrations():
        return register_crud.get_all_registration()
    

registration_service = RegistrationService()




