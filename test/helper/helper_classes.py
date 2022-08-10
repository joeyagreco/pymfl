class MockResponse:
    def __init__(self, data: dict | str, status_code: int, **kwargs):
        self.__data = data
        self.content = kwargs.pop("content", None)
        self.status_code = status_code

    def json(self) -> dict:
        return self.__data
