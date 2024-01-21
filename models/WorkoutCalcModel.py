from dataclasses import dataclass
from random import randint


@dataclass
class WorkoutCalc:
    recent_hh: int = randint(2, 9)
    recent_mm: int = randint(2, 9)
    recent_ss: int = randint(1, 9)
    short_test: int = randint(21, 50)
    goal_hh: int = randint(1, 9)
    goal_mm: int = randint(1, 9)
    goal_ss: int = randint(1, 9)
    long_test: int = randint(21, 50)
    temperature: int = randint(1, 99)
    humidity: int = randint(1, 99)
    wind_speed: int = randint(1, 99)
    critical_power: int = randint(100, 150)
    reserve_work_capacity: int = randint(1, 20)
    race_avg_power_w: int = randint(21, 50)
