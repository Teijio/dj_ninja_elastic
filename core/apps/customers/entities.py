from dataclasses import dataclass
import datetime


@dataclass
class Customer:
    phone: str
    created_at: datetime
