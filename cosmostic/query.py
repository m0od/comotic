from typing import Union, Any


FieldProxyAny = Union["FieldProxy", Any]


class Parameter:
    def __init__(self, name):
        self.name = name


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
