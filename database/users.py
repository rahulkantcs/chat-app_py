from models.user import UserIn, UserOut, UserInDB
from typing import List
from pydantic import EmailStr
from security.helper import get_password_hash, verify_password

async def create_user(user: UserIn, mongodb) -> UserOut | None:
    user_in_db: UserInDB = await mongodb["users"].find_one({'email_address': user.email_address})
    if user_in_db is not None:
        return None
    hashed_password : str = get_password_hash(user.password)
    user_in_db = UserInDB(**user.model_dump(), hashed_password = hashed_password)
    result = await mongodb["users"].insert_one(user_in_db.dict())
    inserted_user: UserOut = await mongodb["users"].find_one({"_id": result.inserted_id}, {'_id': False, 'hashed_password': False})
    return inserted_user

async def login_users(email: EmailStr, password: str, mongodb) -> UserOut | None:
    user_in_db: UserInDB | None = None
    try:
        user_in_db = await mongodb["users"].find_one({'email_address': email }, {'_id': False})
    except Exception as e:
        print(f'Login user not found:: {e}')
    if user_in_db is not None:
        return verify_password(password, user_in_db['hashed_password'])
    else:
        return None

async def getAllUsers(mongodb) -> List[UserOut]:
    users: List[UserOut] = await mongodb["users"].find({}, {'_id': False, 'hashed_password': False}).to_list(100)
    return users

async def getUserByEmail(email_address: str, mongodb) -> UserOut:
    user: UserOut = await mongodb["users"].find_one({'email_address': email_address}, {'_id': False, 'hashed_password': False})
    return user