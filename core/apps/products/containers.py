from functools import lru_cache

import punq

from core.apps.customers.services.auth import AuthService, BaseAuthServive
from core.apps.customers.services.codes import BaseCodeService, DjangoCacheCodeService
from core.apps.customers.services.customers import BaseCustomerService, ORMCustomerService
from core.apps.customers.services.senders import BaseSenderService, DummySenderService
from core.apps.products.services.products import BaseProductService, ORMProductService



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
    container.register(BaseSenderService, DummySenderService)
    container.register(BaseAuthServive, AuthService)
    
    return container
