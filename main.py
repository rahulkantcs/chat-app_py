import uvicorn
from fastapi import FastAPI, Request
from fastapi.responses import RedirectResponse
from fastapi.staticfiles import StaticFiles
from starlette.middleware.cors import CORSMiddleware

from middleweres.process_time import Process_Time
from middleweres.secure_api import Secure_Api
from database.settings import lifespan
from routers.user_router import user_router
from routers.view_router import view_router
from routers.api_router import api_router

from sockets.socket_app import SocketApp
from sockets.socket_manager import socket_manager

app = FastAPI(lifespan=lifespan)
origins = [
    "http://127.0.0.1:7777",
    "http://localhost:7777",
    "localhost:7777",
    "127.0.0.1:7777"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins, 
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.exception_handler(Exception)
async def global_exception_handler(request: Request, exc: Exception):
    # Log the exception
    print(f"Global exception handler caught: {exc}")
    response = RedirectResponse(url='/')
    return response

app.add_middleware(Process_Time)
app.add_middleware(Secure_Api)

app.mount("/static", StaticFiles(directory="static"), name="static")
app.include_router(view_router)
app.include_router(user_router, prefix='/user')
app.include_router(api_router, prefix='/api', tags=['secured'])

socket_manager.mount_to("/", app)
socket_app = SocketApp(app)
socket_app.run()

if __name__=="__main__":
    print("Server Started on http://localhost:7777/")
    uvicorn.run("main:app", host="0.0.0.0", port=7777, lifespan="on", reload=True)