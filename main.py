from fastapi import FastAPI
from routes.user import user_router
from routes.event import event_router



app = FastAPI()
app.include_router(user_router, prefix="/users", tags=["users"])
app.include_router(event_router, prefix="/events", tags=["events"])



