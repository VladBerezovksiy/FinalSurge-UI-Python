import os
from dotenv import load_dotenv

load_dotenv()


class CredData:
    LOGIN = os.getenv("LOGIN")
    PASSWORD = os.getenv("PASSWORD")
