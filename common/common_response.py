from fastapi.responses import JSONResponse
from typing import Any, Optional

class CommonResponse:
    @staticmethod
    def create_response(status_code: int, message: str, data: Optional[Any] = None):
        """
        A common response format for API responses.
        :param status_code: The HTTP status code.
        :param message: The message to be included in the response.
        :param data: Optional data to be included in the response.
        :return: A FastAPI JSONResponse.
        """
        response_body = {
            "status_code": status_code,
            "message": message,
        }
        if data is not None:
            response_body["data"] = data
        return JSONResponse(content=response_body, status_code=status_code)
