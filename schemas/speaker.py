from pydantic import BaseModel


class SpeakerBase(BaseModel):
    name: str
    topic: str

class SpeakerCreate(SpeakerBase):
    pass

class Speaker(SpeakerCreate):
    id: int