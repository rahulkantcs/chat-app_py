from fastapi import APIRouter, Request, Response, HTTPException

from models.user import UserIn, UserOut, UserLogIn
from database.users import create_user, login_users
from security.helper import create_access_token

user_router = APIRouter()

@user_router.post("/create", response_model=UserOut)
async def insert_user(user: UserIn, request: Request, response: Response):
    if not user.password or not user.first_name or not user.last_name or not user.email_address or not user.phone_number:
        raise HTTPException(status_code=400, detail="Missing required fields")
    inserted_user: UserOut = await create_user(user, request.app.mongodb)
    if inserted_user is None :
        raise HTTPException(status_code=402, detail="User already exists")
    token: str = create_access_token(data=inserted_user)
    response.set_cookie(key="x-id-token", value=token)
    return inserted_user

@user_router.post("/login", response_model=UserOut)
async def login_user(user: UserLogIn, request: Request, response: Response) -> UserOut | None:
    print(user)
    user_out: UserOut | None = await login_users(user.email_address, user.password, request.app.mongodb)
    if user_out is None :
        raise HTTPException(status_code=401, detail="User does not exists")
    token: str = create_access_token(user_out.dict())
    response.set_cookie(key="x-id-token", value=token)
    return user_out

@user_router.get("/logout")
async def logout_user(response: Response):
    response.delete_cookie("x-id-token")
    return {"message": "Logged out successfully"}
