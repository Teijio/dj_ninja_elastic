from dataclasses import dataclass


@dataclass(eq=False)
class ServiceException(Exception):
    @property
    def message(self):
        return "App exception occured"
