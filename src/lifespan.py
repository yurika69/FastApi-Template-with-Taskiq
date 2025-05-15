from contextlib import asynccontextmanager
from typing import AsyncGenerator
from fastapi import FastAPI
from src.tkq import broker
import os
from dotenv import load_dotenv
load_dotenv()
redis_url = os.getenv("REDIS_URL")


@asynccontextmanager
async def lifespan(app: FastAPI) -> AsyncGenerator[None, None]:
    if not broker.is_worker_process:
        await broker.startup()
    yield

    if not broker.is_worker_process:
        await broker.shutdown()