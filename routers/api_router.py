from fastapi import APIRouter, Request
from typing import List

from database.users import getAllUsers
from database.chats import getAllChats
from models.user import UserOut
from models.chat import Chat

api_router = APIRouter()
    
@api_router.get("/getUsers")
async def getUsers(request: Request):
    print(f'user in request {request.state.user}')
    current_user = request.state.user
    users : List[UserOut] = await getAllUsers(request.app.mongodb)
    return list(filter(lambda user: user['email_address'] != current_user['email_address'], users))

@api_router.get("/chathistory/{reciver_email}")
async def getChat(request: Request, reciver_email: str):
    current_user = request.state.user
    print(f'current_user {current_user}')
    print(f'reciver_email {reciver_email}')
    chats: List[Chat] = await getAllChats(reciver_email=reciver_email, user_email=current_user['email_address'], mongodb=request.app.mongodb)
    return chats