import time

import allure
from allure_commons.types import AttachmentType
from selenium.common import TimeoutException
from selenium.webdriver import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from base.base_locators import LoginLocators, UserNavigateBarLocators, TopNavigationBarLocators, DailyVitalsLocators, \
    WorkoutListLocators, GearRoutesLocators, TrainingLocators, ResourcesLocators, MessageBoardsLocators
from utils.constants import ThreedSleepValues
from utils.credential import CredData


class BasePage:
    cred = CredData()

    LOGIN_LOCATORS = LoginLocators()
    USER_NAVIG_BAR_LOCATORS = UserNavigateBarLocators()
    TOP_NAVIG_BAR_LOCATORS = TopNavigationBarLocators()
    WORKOUT_LIST_LOCATORS = WorkoutListLocators()
    DAILY_VITALS_LOCATORS = DailyVitalsLocators()
    GEAR_ROUTES_LOCATORS = GearRoutesLocators()
    TRAINING_LOCATORS = TrainingLocators()
    RESOURCES_LOCATORS = ResourcesLocators()
    MESSAGE_BOARDS_LOCATORS = MessageBoardsLocators()

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 15, poll_frequency=1)

    # ********************************* WAITS ***************************************************

    def wait_for_visible(self, locator):
        self.wait.until(EC.visibility_of_element_located(locator))
        return self.get_element(locator)

    def wait_for_elements_contains_text(self, locator, text):
        self.wait.until(EC.text_to_be_present_in_element(locator, text))
        return self.get_element(locator)

    def wait_js_is_loaded(self):
        for _ in range(30):
            if self.driver.execute_script("return document.readyState") == "complete":
                return
            self.make_pause(ThreedSleepValues.SHORT_SLEEP)
        raise TimeoutException("Page isn't loaded")

    # ********************************* ACTIONS ***************************************************

    def click_when_ready(self, locator):
        self.wait_for_visible(locator)
        self.wait.until(EC.element_to_be_clickable(locator)).click()

    def is_element_present(self, locator):
        return bool(self.get_elements(locator))

    def hover_over_element(self, locator):
        actions = ActionChains(self.driver)
        actions.move_to_element(self.get_element(locator)).perform()

    # ********************************* OTHER ***************************************************

    def make_pause(self, second):
        try:
            time.sleep(second)
        except KeyboardInterrupt:
            print("Pause interrupted by user.")
            self.driver.quit()

    def get_element(self, locator):
        return self.driver.find_element(*locator)

    def get_elements(self, list_locator):
        return self.driver.find_elements(*list_locator)

    def get_size(self, locator):
        return len(self.get_elements(locator))

    def make_screenshot(self, screenshot_name):
        allure.attach(
            body=self.driver.get_screenshot_as_png(),
            name=screenshot_name,
            attachment_type=AttachmentType.PNG
        )

    # ********************************* OPERATIONS WITH ELEMENTS ***************************************************

    def select_dropdown_option(self, dropdown_btn, dropdown_view, dropdown_options, index):
        self.click_when_ready(dropdown_btn)
        self.wait_for_visible(dropdown_view)
        list_option = self.get_elements(dropdown_options)
        text_option = list_option[index].text
        list_option[index].click()
        try:
            self.wait_for_elements_contains_text(dropdown_btn, text_option)
        except TimeoutException:
            print("No such option in dropdown")
            self.driver.quit()

    def switch_to_frame(self, locator):
        self.wait_for_visible(locator)
        self.driver.switch_to.frame(self.get_element(locator))

    def switch_to_default_window(self):
        window_handles = self.driver.window_handles
        self.driver.switch_to.window(window_handles[0])

    # ********************************* CHECKS ***************************************************

    def check_for_existence(self, locator):
        self.make_pause(ThreedSleepValues.NORMAL_SLEEP)
        return len(self.get_elements(locator)) > 0

    # ********************************* OPERATIONS WITH FINAL-SURGE ***************************************************

    def login(self, email, password):
        self.wait_for_visible(self.LOGIN_LOCATORS.login_panel)
        self.wait_for_visible(self.LOGIN_LOCATORS.email_input_field).clear()
        self.wait_for_visible(self.LOGIN_LOCATORS.email_input_field).send_keys(email)
        self.wait_for_visible(self.LOGIN_LOCATORS.password_input_field).clear()
        self.wait_for_visible(self.LOGIN_LOCATORS.password_input_field).send_keys(password)
        self.click_when_ready(self.LOGIN_LOCATORS.login_button)
        self.wait_js_is_loaded()
        self.wait_for_visible(self.TOP_NAVIG_BAR_LOCATORS.dashboard_icon).is_enabled()
        self.wait_for_visible(self.TOP_NAVIG_BAR_LOCATORS.calendar_icon).is_enabled()
        self.wait_for_visible(self.TOP_NAVIG_BAR_LOCATORS.workout_calculator_icon).is_enabled()
        self.wait_for_visible(self.TOP_NAVIG_BAR_LOCATORS.other_calculator_icon).is_enabled()
        self.wait_for_visible(self.TOP_NAVIG_BAR_LOCATORS.reports_statistics_icon).is_enabled()
        self.wait_for_visible(self.TOP_NAVIG_BAR_LOCATORS.mail_box_icon).is_enabled()
        self.wait_for_visible(self.TOP_NAVIG_BAR_LOCATORS.print_workouts_icon).is_enabled()
        self.wait_for_visible(self.TOP_NAVIG_BAR_LOCATORS.beta_platforms_icon).is_enabled()

    def logout(self):
        self.click_when_ready(self.USER_NAVIG_BAR_LOCATORS.logout_link)
        self.wait_js_is_loaded()
        self.wait_for_visible(self.LOGIN_LOCATORS.logout_panel)
        self.click_when_ready(self.LOGIN_LOCATORS.account_login_button)
        self.wait_js_is_loaded()
        self.driver.delete_all_cookies()
        self.wait_for_visible(self.LOGIN_LOCATORS.email_input_field)
        self.wait_for_visible(self.LOGIN_LOCATORS.password_input_field)
