from fastapi import APIRouter
from fastapi.responses import StreamingResponse
from database.jsonl_manager import get_list
router = APIRouter()


@router.get('/v1/list')
async def get_list_stream():
    return StreamingResponse(get_list(), media_type='application/x-ndjson')

@router.get('/v1/info')
async def get_info():
    return {'message':'info'}
