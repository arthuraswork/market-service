from fastapi import APIRouter
from fastapi.responses import JSONResponse
exception_router = APIRouter()

@exception_router.get('/error/auth')
def auth_error():
    return JSONResponse(
        content= {'detail': 'Invalid or missing token, use correct token with query ?token='},
        status_code=401,
        headers={'Content-Type':'applicationjson'}

    )