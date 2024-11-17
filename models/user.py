from typing import Optional  # Supports for type hints
from pydantic import BaseModel, EmailStr # Most widely used data validation library for python

class UserIn(BaseModel):
    first_name: str
    last_name: str
    middle_name: Optional[str]
    email_address: EmailStr
    phone_number: str
    password: str

class UserOut(BaseModel):
    first_name: str
    last_name: str
    middle_name: Optional[str]
    email_address: EmailStr
    phone_number: str
    
class UserLogIn(BaseModel):
    email_address: EmailStr
    password: str

class UserInDB(BaseModel):
    _id: str
    first_name: str
    last_name: str
    middle_name: Optional[str]
    email_address: EmailStr
    phone_number: str
    hashed_password: str
