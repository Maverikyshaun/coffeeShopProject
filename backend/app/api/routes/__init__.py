from fastapi import APIRouter

from app.api.routes import cafe

api_router = APIRouter()
api_router.include_router(cafe.router, tags=["cafe"])
