import allure
import pytest
from flaky import flaky

from base.base_test import BaseTest


class TestGearRoutes(BaseTest):

    @pytest.mark.gear_routes
    @flaky(max_runs=2, min_passes=1)
    @allure.severity("Normal")
    def test_01_add_shoes(self):
        self.gear_routes_page.add_shoes()

    @pytest.mark.gear_routes
    @flaky(max_runs=2, min_passes=1)
    @allure.severity("Normal")
    def test_02_add_bikes(self):
        self.gear_routes_page.add_bikes()

    @pytest.mark.gear_routes
    @flaky(max_runs=2, min_passes=1)
    @allure.severity("Normal")
    def test_03_add_routes(self):
        self.gear_routes_page.add_routes()
