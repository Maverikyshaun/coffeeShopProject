from fastapi import APIRouter

from app.api.routes import studio

api_router = APIRouter()
api_router.include_router(studio.router, tags=["studio"])
