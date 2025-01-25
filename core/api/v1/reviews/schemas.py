from datetime import datetime
from pydantic import BaseModel


class ReviewInSchema(BaseModel):
    rating: int
    text: str


class CreateReviewSchema(BaseModel):
    product_id: int
    customer_id: int
    review: ReviewInSchema


class ReviewOutSchema(ReviewInSchema):
    id: int
    created_at: datetime
    updated_at: datetime | None
