import allure

from base.base_page import BasePage
from utils import credential


class LoginPage(BasePage):

    @allure.step("Enter invalid data in 'Login' page")
    def incorrect_credentials_login(self, email, password):
        self.wait_for_visible(self.LOGIN_LOCATORS.login_panel)
        self.wait_for_visible(self.LOGIN_LOCATORS.email_input_field).clear()
        self.wait_for_visible(self.LOGIN_LOCATORS.email_input_field).send_keys(email)
        self.wait_for_visible(self.LOGIN_LOCATORS.password_input_field).clear()
        self.wait_for_visible(self.LOGIN_LOCATORS.password_input_field).send_keys(password)
        self.click_when_ready(self.LOGIN_LOCATORS.login_button)

    @allure.step("Check 'Login' page")
    def check_login_page(self):
        self.incorrect_credentials_login("email1@domain.com", "Temp14%")
        self.login(self.cred.LOGIN, self.cred.PASSWORD)
        self.logout()

    @allure.step("Enter valid data in 'Login' page")
    def verification_on_main_page(self):
        self.login(self.cred.LOGIN, self.cred.PASSWORD)
        self.logout()
