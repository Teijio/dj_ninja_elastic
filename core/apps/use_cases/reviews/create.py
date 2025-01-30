from dataclasses import dataclass

from core.apps.customers.services.customers import BaseCustomerService
from core.apps.products.services.products import BaseProductService
from core.apps.products.services.reviews import BaseReviewService, BaseReviewValidatorService
from core.apps.products.entities import reviews as ReviewEntity


@dataclass
class CreateReviewUseCase:
    review_service: BaseReviewService
    customer_service: BaseCustomerService
    product_service: BaseProductService
    validator_service: BaseReviewValidatorService

    def execute(
        self,
        product_id: int,
        customer_token: str,
        review: ReviewEntity,
    ) -> ReviewEntity:
        # получить продукт
        # проверить валидность токена
        # проверять рейтинг (1 <= R <= 5)
        # проверять текст на длину или цензурность
        customer = self.customer_service.get_by_token(token=customer_token)
        product = self.product_service.get_by_id(product_id=product_id)
        self.validator_service.validate(review=review, customer=customer, product=product)
        saved_rewiew = self.review_service.save_review(product=product, customer=customer, review=review)

        return saved_rewiew
