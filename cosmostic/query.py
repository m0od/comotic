from inspect import Parameter
from typing import Union, Any, TYPE_CHECKING

if TYPE_CHECKING:
    pass

FieldProxyAny = Union["FieldProxy", Any]


def _cmp_expression(syntax: str, op: str, value: Union[Any, Parameter]):
    if isinstance(value, Parameter):
        return "{} {} @{}".format(syntax, op, value.name)
    elif isinstance(value, str):
        return "{} {} '{}'".format(syntax, op, value.strip())
    return "{} {} {}".format(syntax, op, value)


def eq_(syntax: Any, value: Union[Any, Parameter]):
    return _cmp_expression(syntax, "=", value)


def ne_(syntax: Any, value: Union[Any, Parameter]):
    return _cmp_expression(syntax, "!=", value)


def gt_(syntax: Any, value: Union[Any, Parameter]):
    return _cmp_expression(syntax, ">", value)


def gte_(syntax: Any, value: Union[Any, Parameter]):
    return _cmp_expression(syntax, ">=", value)


def lt_(syntax: Any, value: Union[Any, Parameter]):
    return _cmp_expression(syntax, "<", value)


def lte_(syntax: Any, value: Union[Any, Parameter]):
    return _cmp_expression(syntax, "<=", value)


#
# def size_(fields: FieldProxyAny):
#     return _cmp_expression(fields, syntax="ARRAY_SIZE({fields})")
#
#
# def set_intersect_(fields: FieldProxyAny, value: Iterable):
#     return _cmp_expression(
#         fields, syntax="SetIntersect({fields}, {value})", op="", cmp_value=value
#     )


class Parameter:
    def __init__(self, name):
        self.name = name
