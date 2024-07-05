from dataclasses import dataclass
from datetime import date
from random import randint


@dataclass
class Shoes:
    name: str = f"Shoe {date.today().strftime('%m/%d/%Y')}"
    modal: str = "Zero 112"
    cost: int = randint(1, 99)
    starting_distance: int = randint(1, 99)
    distance_alert: int = randint(1, 99)
    notes: str = "AQA TEST"
