from schemas.user import UserCreate
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
    def deactivate_user(user_id: int):
        for user in users:
            if user.id == user_id:
                user.is_active = False
                if not user.is_active:
                    break
                return {"message": "User deactivated successfully"}
        return {"message": "User not found or deleted successfully"}

    @staticmethod
    def get_all_users():
        return users    


user_crud = UserCrud()
