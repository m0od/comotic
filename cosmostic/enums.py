from enum import Enum
from typing import Type, List


class BaseEnum(object):
    @classmethod
    def keys(cls: Type[Enum]) -> List[str]:
        return [item for item in cls.__members__.keys()]

    @classmethod
    def values(cls: Type[Enum]) -> List[str]:
        return [item.value for item in cls.__members__.values()]


class Syntax(BaseEnum, str, Enum):
    ARRAY_CONCAT = "ARRAY_CONCAT"
    ARRAY_CONTAINS = "ARRAY_CONTAINS"
    ARRAY_CONTAINS_ANY = "ARRAY_CONTAINS_ANY"
    ARRAY_CONTAINS_ALL = "ARRAY_CONTAINS_ALL"
    ARRAY_LENGTH = "ARRAY_LENGTH"
    ARRAY_SLIDE = "ARRAY_LENGTH"
