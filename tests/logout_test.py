import allure
import pytest
from flaky import flaky

from base.base_test import BaseTest


class TestLogout(BaseTest):

    @pytest.mark.login
    @flaky(max_runs=2, min_passes=1)
    @allure.severity("Critical")
    def test_01_logout(self):
        self.login_page.login(self.cred.LOGIN, self.cred.PASSWORD)
        self.login_page.logout()
