from fastapi import APIRouter
from app.api.v1.endpoints import auth, legal_ai

api_router = APIRouter()
api_router.include_router(auth.router, prefix="/auth", tags=["auth"])
api_router.include_router(legal_ai.router, prefix="/legal", tags=["legal"])
