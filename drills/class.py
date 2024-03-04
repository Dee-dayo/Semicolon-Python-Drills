from collections import namedtuple
from dataclasses import dataclass
from decimal import Decimal

Player = namedtuple('Player', ['name'])

p1 = Player('franklin')
print(p1)


@dataclass(order=True)
class Akant:
    name: str
    balance: Decimal
    number: int


a1 = Akant('beejay', Decimal('10'), 2090)
print(a1)

