from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import Iterable

from core.apps.customers.entities import CustomerEntity


class BaseSenderService(ABC):
    @abstractmethod
    def send_code(self, customer: CustomerEntity, code: str) -> None: ...


class DummySenderService(BaseSenderService):
    def send_code(self, customer: CustomerEntity, code: str) -> None:
        print(f"Code to user: {customer}, sent: {code}")


class EmailSenderService(BaseSenderService):
    def send_code(self, customer: CustomerEntity, code: str) -> None:
        print(f"Code to user: {customer}, sent via email {code}")


class SmsSenderService(BaseSenderService):
    def send_code(self, customer: CustomerEntity, code: str) -> None:
        print(f"Code to user: {customer}, sent via sms {code}")

# а это пример где множество контейнеров можем передавать и реализовывать в handlers
@dataclass
class ComposedSenderService(BaseSenderService):
    sender_services: Iterable[BaseSenderService]

    def send_code(self, customer: CustomerEntity, code: str) -> None:
        for service in self.sender_services:
            service.send_code(customer, code)
