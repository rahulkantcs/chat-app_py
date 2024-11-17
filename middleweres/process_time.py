
import time
from starlette.middleware.base import BaseHTTPMiddleware

class Process_Time(BaseHTTPMiddleware):
    async def dispatch(self, request, call_next):
        start_time = time.time()
        response = await call_next(request)
        response.headers["X-Process-Time"] = str(time.time() - start_time)
        return response
