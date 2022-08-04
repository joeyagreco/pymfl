from enum import unique, Enum, auto


@unique
class APIResponseType(Enum):
    JSON = auto()
    CONTENT = auto()
