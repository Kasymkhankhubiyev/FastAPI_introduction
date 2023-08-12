from pydantic import BaseModel
from typing import List


class Event(BaseModel):
    id: int
    title: str
    image: str
    description: str
    tags: List[str]
    location: str

    class Config:
        schema_extra = {
            "example": {
                "title": "Event title here",
                "image": "An Image that describes an event, 'http://imagelink/image.png'",
                "description": "In this part we describe am event in detailes",
                "tags": ["event", "besteventever", "pythonevent"],
                "location": "Google Meet"
            }
        }