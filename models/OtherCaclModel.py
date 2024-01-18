from dataclasses import dataclass
from random import randint


@dataclass
class OtherCalc:
    distance: int = randint(1, 99)
    hh: int = randint(1, 9)
    mm: int = randint(1, 9)
    ss: int = randint(1, 9)
    weight: int = randint(21, 50)
    height: int = randint(21, 50)
    age: int = randint(1, 99)
