from models.chat import Chat
from typing import List


async def createChat(chat: Chat, mongodb) -> Chat:
    result = await mongodb["chats"].insert_one(chat.dict())
    inserted_chat: Chat = await mongodb["chats"].find_one({"_id": result.inserted_id}, {'_id': False})
    return inserted_chat

async def getAllChats(reciver_email, user_email, mongodb) -> List[Chat]:
    print(f'reciver_email in all chats {reciver_email}')
    chatsFrom: List[Chat] | None = await mongodb["chats"].find(
        {'sender': user_email, 'receiver': reciver_email},
        {'_id': False}).sort({'sentOn': -1}).to_list(100)
    chatsTo: List[Chat] | None = await mongodb["chats"].find(
        {'sender': reciver_email, 'receiver': user_email},
        {'_id': False}).sort({'sentOn': -1}).to_list(100)
    chatsFrom = [] if chatsFrom is None else chatsFrom
    chatsTo = [] if chatsTo is None else chatsTo
    print(f'chatsFrom {chatsFrom}')
    print(f'chatsTo {chatsTo}')
    allChats = chatsFrom + chatsTo
    return sorted(allChats, key=lambda chat: chat['sentOn'])