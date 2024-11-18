from django.http import HttpRequest
from ninja import Router

from core.api.v1.products.schemas import ProductListSchema
from core.apps.products.services.products import BaseProductService, ORMProductService

router = Router(tags=["Products"])

@router.get("", response=ProductListSchema)
def get_product_list_handler(request: HttpRequest) -> ProductListSchema:
    service: BaseProductService = ORMProductService()
    product_list = service.get_product_list()
    return product_list
