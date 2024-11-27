import json
from typing import Any, Union, List, Iterable

from core.cosmos.query import Parameter, eq_, ne_, gt_, gte_, lt_, lte_


class FieldProxy:

    def __init__(self, name, _type: Any = None, is_function: bool = False):
        self.name = name
        self.type = _type
        self.is_function = is_function

    def __pos__(self):
        return self.name

    @property
    def __name__(self):
        if not self.is_function:
            return f"c.{+self}"
        return f"{+self}"

    # def __eq__(self, value):
    #     return self.eq(value)
    #
    # def __ne__(self, value):
    #     return self.ne(value)
    #
    # def __gt__(self, value):
    #     return self.gt(value)
    #
    # def __lt__(self, value):
    #     return self.lt(value)
    #
    # def __le__(self, value):
    #     return self.lte(value)
    #
    # def __ge__(self, value):
    #     return self.gte(value)

    def eq(self, value: Union[Any, Parameter]):
        """Equality comparison operator."""
        return eq_(self.__name__, value)

    def ne(self, value: Union[Any, Parameter]):
        """Inequality comparison operator."""
        return ne_(self.__name__, value)

    def gt(self, value: Union[Any, Parameter]):
        """Greater than (strict) comparison operator (i.e. >)."""
        return gt_(self.__name__, value)

    def gte(self, value: Union[Any, Parameter]):
        """Greater than or equal comparison operator (i.e. >=)."""
        return gte_(self.__name__, value)

    def lt(self, value: Union[Any, Parameter]):
        """Less than (strict) comparison operator (i.e. <)."""
        return lt_(self.__name__, value)

    def lte(self, value: Union[Any, Parameter]):
        """Less than or equal comparison operator (i.e. <=)."""
        return lte_(self.__name__, value)

    def size(self, _type: Any = str):
        """Number of elements in array"""
        if _type == classmethod:
            return FieldProxy(name=f"ARRAY_LENGTH({self.__name__})", is_function=True)
        else:
            return f"ARRAY_LENGTH({self.__name__})"

    def set_intersect(self, value: Union[List, Parameter], _type: Any = str):
        if isinstance(value, Parameter):
            value = f"@{value.name}"
        if _type == classmethod:
            return FieldProxy(
                name=f"SetIntersect({self.__name__}, {value})", is_function=True
            )
        return f"SetIntersect({self.__name__}, {value})"

    def __contains__(self, syntax: str, value: Union[Any, Parameter], full_match):
        if isinstance(value, Parameter):
            value = f"@{value.name}"
        elif isinstance(value, Iterable):
            value = json.dumps(value)[1:-1]
        return f"{syntax}({self.__name__}, {value}, {str(full_match).lower()})"

    def contains(self, value: Union[Any, Parameter], full_match: bool = False):
        return self.__contains__("ARRAY_CONTAINS", value, full_match)

    def contains_all(self, value: Union[Any, Parameter], full_match: bool = False):
        return self.__contains__("ARRAY_CONTAINS_ALL", value, full_match)

    def contains_any(self, value: Union[Any, Parameter], full_match: bool = False):
        return self.__contains__("ARRAY_CONTAINS_ANY", value, full_match)
