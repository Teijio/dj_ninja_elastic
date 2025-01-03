from abc import ABC, abstractmethod


class BaseAuthServive(ABC):
    @abstractmethod
    def authorize(self, phone: str): ...

    @abstractmethod
    def confirm(self, token: str): ...

