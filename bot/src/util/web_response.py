from dataclasses import dataclass
from typing import TypeVar, Generic

T = TypeVar('T')


class ErrorResponseData:
    def __init__(self, message_code=10001, message='系统错误'):
        self.code = message_code
        self.message = message
        # self.domain = HTTPException.get_request_domain()

    def to_dict(self):
        return {
            'code': self.code,
            'message': self.message
            # 'domain': self.domain
        }


class WebResponse(Generic[T]):
    def __init__(self, data: T = None, error: ErrorResponseData = None):
        self.data = data
        self.error = error

    @property
    def _json(self):
        return {
            'error': self.error,
            'data': self.data
        }

    @staticmethod
    def build_data(data):
        resp = WebResponse(data=data)
        return resp._json

    @staticmethod
    def build_custom_error(error: ErrorResponseData):
        resp = WebResponse(error=error)
        return resp._json

    @staticmethod
    def build_error(message_code=10001, message='系统错误'):
        error = ErrorResponseData(message_code, message)
        resp = WebResponse(error=error)
        return resp._json
