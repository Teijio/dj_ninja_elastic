from abc import ABC, abstractmethod
import random

from django.core.cache import cache

from core.apps.customers.entities import Customer
from core.apps.customers.exceptions.codes import CodeNotEqualException, CodeNotFoundException


class BaseCodeService(ABC):
    @abstractmethod
    def generate_code(self, customer: Customer) -> str: ...

    @abstractmethod
    def validate_code(self, code: str, customer: Customer) -> None: ...


class DjangoCacheCodeService(BaseCodeService):
    def generate_code(self, customer: Customer) -> str:
        code = str(random.randint(100000, 999999))
        cache.set(customer.phone, code)
        return code

    def validate_code(self, code: str, customer: Customer) -> None:
        cached_code = cache.get(customer.phone, code)

        if cached_code is None:
            raise CodeNotFoundException(code=code)
        if cached_code != code:
            raise CodeNotEqualException(code=code, cache_code=cached_code, customer_phone=customer.phone)

        cache.delete(customer.phone)
