import json
import os.path

import pytest

from utils.driver_factory import DriverFactory

# Path to run test from 'Terminal'
# CONFIG_PATH = os.path.abspath("../config.json")
CONFIG_PATH = os.path.abspath("../FinalSurge-UI-Python/config.json")


@pytest.fixture(scope="session")
def config():
    config_file = open(CONFIG_PATH)
    return json.load(config_file)


@pytest.fixture(autouse=True, scope="class")
def get_driver(request, config):
    driver = DriverFactory.get_driver(config)
    driver.get(config["base_url"])
    driver.implicitly_wait(config["timeout"])
    request.cls.get_driver = driver
    yield driver
    driver.quit()
