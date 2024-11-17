from pydantic import BaseModel, EmailStr # Most widely used data validation library for python

class Chat(BaseModel):
    sender: EmailStr
    receiver: EmailStr
    message: str
    sentOn: int