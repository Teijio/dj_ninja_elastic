from typing import Any, Generic, TypeVar

from pydantic import Field
from ninja import Schema

from core.api.filters import PaginationOut


TData = TypeVar("TData")
TListItem = TypeVar("TListSchema")


class PingResponseSchema(Schema):
    result: bool


class ListPaginatedResponse(Schema, Generic[TListItem]):
    items: list[TListItem]
    pagination: PaginationOut


class ApiResponse(Schema, Generic[TData]):
    data: TData | dict = Field(default_factory=dict)
    meta: dict[str, Any] = Field(default_factory=dict)
    errors: list[Any] | dict = Field(default_factory=dict)
