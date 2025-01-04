from abc import ABC, abstractmethod
import random

from django.core.cache import cache

from core.apps.customers.entities import CustomerEntity


class BaseCodeService(ABC):
    @abstractmethod
    def generate_code(self, customer: CustomerEntity) -> str: ...

    @abstractmethod
    def validate_code(self, code: str, customer: CustomerEntity) -> None: ...


class DjangoCacheCodeService(BaseCodeService):
    def generate_code(self, customer: CustomerEntity) -> str:
        code = str(random.randint(100000, 999999))
        cache.set(customer.phone, code)
        return code

    def validate_code(self, code: str, customer: CustomerEntity) -> None:
        code = cache.get(customer.phone, code)
        
