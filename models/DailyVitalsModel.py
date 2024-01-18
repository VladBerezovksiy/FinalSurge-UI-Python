from dataclasses import dataclass
from datetime import date
from random import randint


@dataclass
class DailyVitals:
    date_string = date.today().strftime("%m/%d/%Y")
    date: str = date_string[1:] if date_string[0] == "0" else date_string
    steps: int = randint(1, 99)
    calories: int = randint(1, 99)
    weight: int = randint(1, 99)
    body_fat: int = randint(1, 99)
    water: int = randint(1, 99)
    muscle_mass: int = randint(1, 99)
    resting_hr: int = randint(1, 99)
    variability_hr: int = randint(1, 99)
    sleep_hours: int = 5
    total_time_awake: int = 6
    blood_pressure: int = randint(1, 99)
    blood_pressure1: int = randint(1, 99)
    notes: str = "AQA TEST"
