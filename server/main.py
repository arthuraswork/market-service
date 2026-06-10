from fastapi import FastAPI, Request
from fastapi.responses import RedirectResponse
from backend.routers import router as backend_router
from backend.errors import exception_router
from load_tokens import load_tokens
from database.db import lifespan




tokens = set(load_tokens())

app = FastAPI(lifespan=lifespan)

app.include_router(backend_router)
app.include_router(exception_router)

@app.middleware('http')
async def check_token(request: Request, call_next):
    token = request.query_params.get('token')
    if not token or token not in tokens:
        return RedirectResponse('/error/auth', status_code=401)
    else:
        response = await call_next(request)
        return response