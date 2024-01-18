from dataclasses import dataclass
from datetime import date, datetime
from random import randint


@dataclass
class Workout:
    date: str = date.today().strftime("%m%d%y")  # Assuming short date format
    time: str = datetime.now().strftime("%H:%M")
    name: str = f"AQA {date.today().strftime("%m/%d/%Y")}"
    description: str = "AQA TEST"
    distance: int = randint(1, 99)
    duration: int = randint(1, 99)
    pace: str = datetime.now().strftime("%H:%M")
    overall_place: int = randint(1, 99)
    age_place: int = randint(1, 99)
    new_library: str = f"NEW LIBRARY {date.today().strftime("%m/%d/%Y")}"
    code: int = randint(1, 99)
