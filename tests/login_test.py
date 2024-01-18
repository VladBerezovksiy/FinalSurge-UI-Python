import allure
from flaky import flaky
import pytest

from base.base_test import BaseTest


class TestLogin(BaseTest):

    @pytest.mark.login
    @flaky(max_runs=2, min_passes=1)
    @allure.severity("Normal")
    def test_01_check_login_page(self):
        self.login_page.check_login_page()

    @pytest.mark.login
    @flaky(max_runs=2, min_passes=1)
    @allure.severity("Critical")
    def test_02_verification_on_the_main_page(self):
        self.login_page.verification_on_main_page()
