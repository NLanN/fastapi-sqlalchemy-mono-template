from fastapi import APIRouter

from src.app.controllers.auth import router as auth_router
from src.app.controllers.items import router as item_router
from src.app.controllers.test import router as test_router
from src.app.controllers.users import router as user_router

api_router = APIRouter()
api_router.include_router(test_router, prefix="/test", tags=["test"])
api_router.include_router(auth_router, prefix="/auth", tags=["auth"])
api_router.include_router(user_router, prefix="/user", tags=["user"])
api_router.include_router(item_router, prefix="/item", tags=["item"])
