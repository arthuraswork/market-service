from fastapi import APIRouter

router = APIRouter()


@router.get('/v1/list')
async def get_list():
    return {'message':'list','value':[]}

@router.get('/v1/info')
async def get_info():
    return {'message':'info'}