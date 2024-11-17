import time

from security.helper import decode
from database.chats import createChat
from models.chat import Chat

class SocketApp:
    def __init__(self, app):
        self.app = app
        self.connections = {}

    def on_connect(self, sid, env, auth):
        print(f"New Client Connected to This id :{str(sid)}")
        user = decode(auth["x-id-token"])
        user['sid'] = sid
        print(f"user :{user}")
        self.connections[user['email_address']] = user

    def on_disconnect(self, sid):
        print(f"Client Disconnected from This id :{str(sid)}")

    async def on_private_message(self, sid, data):
        print(f"Message from {sid} : {data}")
        chat = Chat(sender=data['from'], receiver=data['to'], message=data['message'], sentOn=round(time.time() * 1000))
        print(f"Chat : {chat}")
        await createChat(chat, self.app.mongodb)
        to_sid = self.connections[data['to']]['sid']
        await self.app.socket_manager.emit('private message', data, to=to_sid)

    def run(self):
        self.app.socket_manager.on('connect')(self.on_connect)
        self.app.socket_manager.on('disconnect')(self.on_disconnect)
        self.app.socket_manager.on('private message')(self.on_private_message)
