from dataclasses import dataclass
from datetime import date
from random import randint


@dataclass
class Bikes:
    name: str = f"Bike {date.today().strftime('%m/%d/%Y')}"
    modal: str = "Zero 121"
    cost: int = randint(1, 9)
    starting_distance: int = randint(1, 9)
    distance_alert: int = randint(1, 9)
    notes: str = "AQA TEST"
