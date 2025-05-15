from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from . import lifespan
from src.routes import router
import socket

def get_app() -> FastAPI:
    app = FastAPI(
        title="api_template",
        docs_url="/docs",
        lifespan=lifespan.lifespan,
    )
    app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
    )
    app.include_router(router)

    return app