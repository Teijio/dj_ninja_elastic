from functools import lru_cache

import punq

from core.apps.customers.services.auth import AuthService, BaseAuthServive
from core.apps.customers.services.codes import BaseCodeService, DjangoCacheCodeService
from core.apps.customers.services.customers import BaseCustomerService, ORMCustomerService
from core.apps.customers.services.senders import (
    BaseSenderService,
    ComposedSenderService,
    DummySenderService,
    EmailSenderService,
    SmsSenderService,
)
from core.apps.products.services.products import BaseProductService, ORMProductService
from core.apps.products.services.reviews import BaseReviewService, BaseReviewValidatorService, ComposeReviewValidatorService, ORMReviewService
from core.apps.use_cases.reviews.create import CreateReviewUseCase


@lru_cache(1)
def get_container() -> punq.Container:
    return _initialize_container()


def _initialize_container() -> punq.Container:
    container = punq.Container()

    # init products
    container.register(BaseProductService, ORMProductService)

    # init customers
    container.register(BaseCustomerService, ORMCustomerService)
    container.register(BaseCodeService, DjangoCacheCodeService)
    # Пример когда передаем множество параметров
    container.register(
        BaseSenderService,
        ComposedSenderService,
        sender_services=(
            EmailSenderService(),
            SmsSenderService(),
        ),
    )
    container.register(BaseAuthServive, AuthService)
    container.register(BaseReviewService, ORMReviewService)
    container.register(BaseReviewValidatorService, ComposeReviewValidatorService, validators=[])
    container.register(CreateReviewUseCase)
    return container
