from fastapi import APIRouter
from api.movies import movies_router

api_router = APIRouter(prefix="/api")

api_router.include_router(movies_router)
