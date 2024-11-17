import socketio

class SocketManager:
    def __init__(self):
        self.server = socketio.AsyncServer(
            cors_allowed_origins="*",
            async_mode="asgi",
            logger=True,
            engineio_logger=True,
        )
        self.app = socketio.ASGIApp(self.server, socketio_path='/chats')
        self.connections = {}

    @property
    def on(self):
        return self.server.on

    @property
    def send(self):
        return self.server.send
    
    @property
    def emit(self):
        return self.server.emit

    def mount_to(self, path: str, app):
        app.mount(path, self.app)
        app.socket_manager = self

socket_manager = SocketManager()
