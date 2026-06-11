import asyncpg
from typing import Literal
import asyncio
import json
from enum import Enum

class Queries(Enum):
    GET_LINES = 'SELECT * FROM goods'
    GET_OBJECT_CODE = 'SELECT * FROM GOODS WHERE code = $1'
    GET_OBJECT_TITLE = 'SELECT * FROM GOODS WHERE title = $1'
    INCR_MINUS_OBJECT_TITLE = 'UPDATE goods SET count = count - 1 WHERE title = $1' 
    INCR_PLUS_OBJECT_TITLE = 'UPDATE goods SET count = count + 1 WHERE title = $1' 
    INCR_MINUS_OBJECT_CODE = 'UPDATE goods SET count = count - 1 WHERE code = $1' 
    INCR_PLUS_OBJECT_CODE = 'UPDATE goods SET count = count + 1 WHERE code = $1' 



class Database:

    def __init__(self):
        self.conn: asyncpg.Connection = None

    async def select_config(self, path= 'secrets/dbconn.json'):
        with open(path, 'r') as f:
            return json.load(f)

    async def incr_minus(self, by: Literal['title', 'code'], value: str):
        await self.conn.execute(Queries.INCR_MINUS_OBJECT_TITLE.value if by == 'title' else Queries.INCR_MINUS_OBJECT_CODE.value, value)

    async def incr_plus(self, by: Literal['title', 'code'], value: str):
        await self.conn.execute(Queries.INCR_PLUS_OBJECT_TITLE.value if by == 'title' else Queries.INCR_PLUS_OBJECT_CODE.value, value)

    async def connection(self):
        conn_data = await self.select_config()
        conn = await asyncpg.connect(**conn_data)
        self.conn = conn
    
    async def get_lines(self):
        rows = await self.conn.fetch(Queries.GET_LINES.value)
        for row in rows:
            yield dict(row)

    async def get_object(self, by: Literal['title', 'code'], value: str):
        object = await self.conn.fetchrow(Queries.GET_OBJECT_TITLE.value if by == 'title' else Queries.GET_OBJECT_CODE.value, value)
        return object

    async def close(self):
        await self.conn.close()
