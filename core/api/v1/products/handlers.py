from django.http import HttpRequest
from django.apps import apps
from ninja import Query, Router

from core.api.filters import PaginationOut, PaginationIn
from core.api.schemas import ApiResponse, ListPaginatedResponse
from core.api.v1.products.filters import ProductFilters
from core.api.v1.products.schemas import ProductSchema
from core.project.containers import get_container
from core.apps.products.filters.products import ProductFilters as ProductFiltersEntity
from core.apps.products.services.products import BaseProductService


router = Router(tags=["Products"])


@router.get("", response=ApiResponse[ListPaginatedResponse[ProductSchema]])
def get_product_list_handler(
    request: HttpRequest,
    filters: Query[ProductFilters],
    pagination_in: Query[PaginationIn],
) -> ApiResponse[ListPaginatedResponse[ProductSchema]]:
    container = get_container()
    service: BaseProductService = container.resolve(BaseProductService)
    product_list = service.get_product_list(
        filters=ProductFiltersEntity(search=filters.search),
        pagination=pagination_in,
    )
    product_count = service.get_product_count(filters=filters)
    items = [ProductSchema.from_entity(obj) for obj in product_list]
    pagination_out = PaginationOut(offset=pagination_in.offset, limit=pagination_in.limit, total=product_count)

    return ApiResponse(data=ListPaginatedResponse(items=items, pagination=pagination_out))
