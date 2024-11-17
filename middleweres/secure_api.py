from starlette.middleware.base import BaseHTTPMiddleware
from fastapi.responses import HTMLResponse, RedirectResponse

from security.helper import decode

class Secure_Api(BaseHTTPMiddleware):
    
    SECURE_PATH = "/api"
    
    async def dispatch(self, request, call_next):
        path = request.url.path
        if path.__contains__(self.SECURE_PATH):
            user = self.isValid(request.cookies.get("x-id-token"))
            request.state.user = user
        return await call_next(request)

    def isValid(self, token: str) -> bool:
        if not token:
            return RedirectResponse("/")
        return decode(token)
        