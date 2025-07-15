from fastapi import HTTPException
from schemas.user import UserCreate, UserUpdate
from database import users
from models import User as UserModel


class UserCrud:

    @staticmethod
    def create_user(user_data: UserCreate):
        user_id = len(users) + 1
        user = UserModel(id=user_id, **user_data.model_dump())
        users.append(user)
        return user
                                    
    
    @staticmethod
    def get_users_by_id(user_id: int):
        for user in users:
            if user.id == user_id:
                return user
        return {"message": "User not exist"}
    
    @staticmethod
    def update_user(user_id: int, user_data: UserUpdate):
        for user in users:
            if user.id == user_id:
                if user_data.name:
                    user.name = user_data.name
                if user_data.email:
                    user.email = user_data.email
                return user 
        raise HTTPException(status_code=404, detail="User not found")           

    
    @staticmethod
    def deactivate_user(user_id: int):
        for user in users:
            if user.id == user_id:
                if not user.is_active:
                    raise HTTPException(status_code=403, detail="User is not active")
                user.is_active = False
                return {"message": "User deactivated successfully"}
        raise HTTPException(status_code=404, detail="User not found")

        
    @staticmethod
    def get_all_users():
        return users    


user_crud = UserCrud()
