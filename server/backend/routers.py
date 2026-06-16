from fastapi import APIRouter, Depends, Request
from fastapi.responses import StreamingResponse
from typing import Literal
from database.db import db
import json

router = APIRouter()

@router.get('/v1/list')
async def get_list_stream():
    async def generate():
        async for r in db.get_lines():
            yield json.dumps(r, ensure_ascii=False) + '\n'

    return StreamingResponse(
        generate(),
        media_type='application/x-ndjson'
        )

@router.get('/v1/info')
async def get_info(by: Literal['title','code'], value: str):
    obj = await db.get_object(by, value)
    return obj

@router.patch('/v1/incr_minus')
async def get_info(by: Literal['title','code'], value: str):
    await db.incr_minus(by, value)

@router.patch('/v1/incr_plus')
async def get_info(by: Literal['title','code'], value: str):
    await db.incr_plus(by, value)
