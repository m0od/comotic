from typing import Any

from bson import ObjectId
from pydantic import BaseModel, field_serializer, Field
from pydantic._internal._model_construction import ModelMetaclass

from cosmostic.query.field import FieldProxy


class MetaModel(ModelMetaclass):
    def __new__(mcs, name, bases, namespace, **kwargs):
        cls = super().__new__(mcs, name, bases, namespace, **kwargs)
        # print(namespace)
        for k, v in namespace.get("__annotations__", {}).items():
            setattr(cls, k, FieldProxy(name=k, _type=v))
        return cls

    def __pos__(self):
        return f"{self.__name__}"


class Model(BaseModel, metaclass=MetaModel):
    id: str = Field(default_factory=ObjectId)

    @field_serializer("id", check_fields=False)
    def serialize_id(self, value: Any, _info):
        return str(value)
