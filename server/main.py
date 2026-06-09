from fastapi import FastAPI, Request, HTTPException
from backend.routers import router as backend_router
from load_tokens import load_tokens
app = FastAPI()
app.include_router(backend_router)

tokens = load_tokens()

@app.middleware('http')
async def check_token(request: Request, call_next):
    if request.query_params.get('token') in tokens:
        response = await call_next(request)
        return response
    raise HTTPException(401, 'Invalid token')

@app.middleware('http')
async def log(request: Request, call_next):
    response = await call_next(request)
    return response