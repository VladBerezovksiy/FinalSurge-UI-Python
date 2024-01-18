from dataclasses import dataclass
from datetime import date, datetime
from random import randint


@dataclass
class Routes:
    name: str = f"Route {date.today().strftime("%m/%d/%Y")}"
    distance: int = randint(1, 99)
    route_record: str = datetime.now().strftime("%H:%M")
    date_record: str = date.today().strftime("%m/%d/%Y")
    notes: str = "AQA TEST"
