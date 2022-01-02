from src.schemas.base import APIResponse


class TestResponse(APIResponse):
    data: str = None
    code = 200
