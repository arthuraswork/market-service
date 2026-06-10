import asyncpg
import asyncio
import json

async def conn_func(path= 'secrets/dbconn.json'):
    with open(path, 'r') as f:
        return json.load(f)

async def connection():
    conn_data = await conn_func()
    conn = await asyncpg.connect(
        **conn_data
    )

    rows = await conn.fetch('select * from goods')
    for row in rows:
        yield dict(row)  
    await conn.close()


asyncio.run(connection())