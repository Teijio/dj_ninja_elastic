from datetime import datetime
from django.http import HttpRequest
from ninja import Router
from ninja.errors import HttpError

from core.api.schemas import ApiResponse
from core.api.v1.customers.schemas import AuthInSchema, AuthOutSchema, TokenInSchema, TokenOutSchema
from core.api.v1.reviews.schemas import ReviewInSchema, ReviewOutSchema
from core.apps.common.exceptions import ServiceException
from core.apps.customers.services.auth import BaseAuthServive
from core.project.containers import get_container

router = Router(tags=["Reviews"])


@router.post("{product_id}/rewviews", response=ApiResponse[ReviewOutSchema], operation_id="createReview")
def create_review(request: HttpRequest, product_id: int, schema: ReviewInSchema) -> ApiResponse[ReviewOutSchema]:
    return ApiResponse(
        data=ReviewOutSchema(
            rating=1,
            text="hello",
            id="1",
            created_at=datetime.now(),
            updated_at=None,
        )
    )
