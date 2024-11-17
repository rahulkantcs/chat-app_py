import json
from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

from security.helper import decode
from database.users import getUserByEmail

view_router = APIRouter()

templates = Jinja2Templates(directory="views")

@view_router.get("/", response_class=HTMLResponse)
async def login(request: Request):
    return templates.TemplateResponse(
        request=request, name="login.html"
    )

@view_router.get("/register", response_class=HTMLResponse)
async def register(request: Request):
    return templates.TemplateResponse(
        request=request, name="register.html"
    )

@view_router.get("/users", response_class=HTMLResponse)
async def users(request: Request):
    payload = decode(request.cookies.get("x-id-token"))
    return templates.TemplateResponse(
        request=request, name="users.html"
    )

@view_router.get("/chat/{reciver_email}", response_class=HTMLResponse)
async def users(request: Request, reciver_email: str):
    payload = decode(request.cookies.get("x-id-token"))
    reciver= await getUserByEmail(reciver_email, request.app.mongodb)
    return templates.TemplateResponse(
        "chat.html", {"request": request, "reciver": json.dumps(reciver, ensure_ascii=True), "user": json.dumps(payload, ensure_ascii=True)} 
    )
