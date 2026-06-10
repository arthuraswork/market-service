from database.postgre_manager import Database
from fastapi import FastAPI
from contextlib import asynccontextmanager

db = Database()

@asynccontextmanager
async def lifespan(api: FastAPI):
    await db.connection()
    yield
    await db.close()