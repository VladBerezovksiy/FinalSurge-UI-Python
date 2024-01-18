import allure
import pytest
from flaky import flaky

from base.base_test import BaseTest


class TestDailyVitals(BaseTest):

    @pytest.mark.daily_vitals
    @flaky(max_runs=2, min_passes=1)
    @allure.severity("Normal")
    def test_01_check_view_and_vitals(self):
        self.daily_vitals_page.add_daily_and_vitals()
