from fastapi import HTTPException
from schemas.registration import RegistrationCreate
from models import Registration as RegistrationModel
from database import registrations
from datetime import date

class RegistrationCrud:

    @staticmethod
    def create_event_registration(registration_data: RegistrationCreate):
        for reg in registrations:
            if reg.user_id == registration_data.user_id and reg.event_id == registration_data.event_id:
                raise HTTPException(status_code=400, detail="User already registered for this event")
        registration_id = len(registrations) + 1
        registered = RegistrationModel(
            id=registration_id,
            registration_date=date.today(),
            **registration_data.model_dump()
        )
        registrations.append(registered)
        return registered

    @staticmethod
    def get_all_registration():
        return registrations

    @staticmethod
    def get_registration_user_id(user_id: int):
        user_regs = []
        for reg in registrations:
            if reg.user_id == user_id:
                user_regs.append(reg)
        if not user_regs:
            raise HTTPException(status_code=404, detail="User Registration not found")
        return user_regs
    
    @staticmethod
    def get_event_registration(event_id: int):
        event_regs = []
        for reg in registrations:
            if reg.event_id == event_id:
                event_regs.append(reg)
        if not event_regs:
            raise HTTPException(status_code=404, detail="No registrations found for this event")
        return event_regs        
    


    @staticmethod
    def mark_attendance(registration_id: int):
        for reg in registrations:
            if reg.id == registration_id:
                reg.attended = True
                return reg
        raise HTTPException(status_code=404, detail="Registration not found")

    @staticmethod
    def is_user_registered(event_id: int, user_id: int):
        for reg in registrations:
            if reg.user_id == user_id and reg.event_id == event_id:
                return True
        return False
    




register_crud = RegistrationCrud()


