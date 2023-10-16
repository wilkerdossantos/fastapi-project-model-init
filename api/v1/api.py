from fastapi import APIRouter
from api.v1.endpoints import endpoint


api_router = APIRouter()

api_router.include_router(
    endpoint.router, prefix='/endpoint', tags=["endpoint"])
