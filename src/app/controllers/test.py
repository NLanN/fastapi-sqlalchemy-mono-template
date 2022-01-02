from fastapi import APIRouter

from src.schemas.test import TestResponse

router = APIRouter()


@router.get(
    "/index",
    response_model=TestResponse,
    responses={200: {"model": TestResponse}},
)
def test_connection():
    return {"code": 200, "data": "hello"}
