import allure
from selenium.webdriver.common.by import By

from base.base_page import BasePage
from locators.daily_vitals_locators import DailyVitalsPageLocators
from models.DailyVitalsModel import DailyVitals
from utils.constants import ThreedSleepValues


class DailyVitalsPage(BasePage):
    DAILY_VITALS_PAGE_LOCATORS = DailyVitalsPageLocators()

    @allure.step("Add Daily Vitals")
    def add_daily_and_vitals(self):
        self.login(self.cred.LOGIN, self.cred.PASSWORD)
        self.hover_over_element(self.DAILY_VITALS_LOCATORS.daily_vitals_btn)
        self.click_when_ready(self.DAILY_VITALS_LOCATORS.view_add_vitals_btn)
        self.select_dropdown_option(self.DAILY_VITALS_PAGE_LOCATORS.select_date_dropdown,
                                    self.DAILY_VITALS_PAGE_LOCATORS.select_date_dropdown_view,
                                    self.DAILY_VITALS_PAGE_LOCATORS.select_date_dropdown_options, 1)

        for link in self.get_elements(self.DAILY_VITALS_PAGE_LOCATORS.date_links):
            if DailyVitals.date in link.text:
                link.click()
                break
        self.make_pause(ThreedSleepValues.NORMAL_SLEEP)
        self.wait_for_visible(self.DAILY_VITALS_PAGE_LOCATORS.steps_input_field).clear()
        self.wait_for_visible(self.DAILY_VITALS_PAGE_LOCATORS.steps_input_field).send_keys(DailyVitals.steps)
        self.wait_for_visible(self.DAILY_VITALS_PAGE_LOCATORS.calories_input_field).clear()
        self.wait_for_visible(self.DAILY_VITALS_PAGE_LOCATORS.calories_input_field).send_keys(DailyVitals.calories)
        self.wait_for_visible(self.DAILY_VITALS_PAGE_LOCATORS.weight_input_field).clear()
        self.wait_for_visible(self.DAILY_VITALS_PAGE_LOCATORS.weight_input_field).send_keys(DailyVitals.weight)
        self.wait_for_visible(self.DAILY_VITALS_PAGE_LOCATORS.body_fats_input_field).clear()
        self.wait_for_visible(self.DAILY_VITALS_PAGE_LOCATORS.body_fats_input_field).send_keys(DailyVitals.body_fat)
        self.wait_for_visible(self.DAILY_VITALS_PAGE_LOCATORS.water_percent_input_field).clear()
        self.wait_for_visible(self.DAILY_VITALS_PAGE_LOCATORS.water_percent_input_field).send_keys(DailyVitals.water)
        self.wait_for_visible(self.DAILY_VITALS_PAGE_LOCATORS.muscle_mass_input_field).clear()
        self.wait_for_visible(self.DAILY_VITALS_PAGE_LOCATORS.muscle_mass_input_field).send_keys(
            DailyVitals.muscle_mass)
        self.wait_for_visible(self.DAILY_VITALS_PAGE_LOCATORS.resting_hr_input_field).clear()
        self.wait_for_visible(self.DAILY_VITALS_PAGE_LOCATORS.resting_hr_input_field).send_keys(
            DailyVitals.resting_hr)
        self.wait_for_visible(self.DAILY_VITALS_PAGE_LOCATORS.hr_variability_input_field).clear()
        self.wait_for_visible(self.DAILY_VITALS_PAGE_LOCATORS.hr_variability_input_field).send_keys(
            DailyVitals.variability_hr)
        self.wait_for_visible(self.DAILY_VITALS_PAGE_LOCATORS.sleep_hours_input_field).clear()
        self.wait_for_visible(self.DAILY_VITALS_PAGE_LOCATORS.sleep_hours_input_field).send_keys(
            DailyVitals.sleep_hours)
        self.wait_for_visible(self.DAILY_VITALS_PAGE_LOCATORS.awake_time_input_field).clear()
        self.wait_for_visible(self.DAILY_VITALS_PAGE_LOCATORS.awake_time_input_field).send_keys(
            DailyVitals.total_time_awake)
        self.wait_for_visible(self.DAILY_VITALS_PAGE_LOCATORS.heals_notes_input_field).clear()
        self.wait_for_visible(self.DAILY_VITALS_PAGE_LOCATORS.heals_notes_input_field).send_keys(
            DailyVitals.notes)

        self.select_dropdown_option(self.DAILY_VITALS_PAGE_LOCATORS.sleep_amount_dropdown,
                                    self.DAILY_VITALS_PAGE_LOCATORS.sleep_amount_dropdown_view,
                                    self.DAILY_VITALS_PAGE_LOCATORS.sleep_amount_dropdown_options, 2)
        self.select_dropdown_option(self.DAILY_VITALS_PAGE_LOCATORS.sleep_quality_dropdown,
                                    self.DAILY_VITALS_PAGE_LOCATORS.sleep_quality_dropdown_view,
                                    self.DAILY_VITALS_PAGE_LOCATORS.sleep_quality_dropdown_options, 2)
        self.select_dropdown_option(self.DAILY_VITALS_PAGE_LOCATORS.stress_amount_dropdown,
                                    self.DAILY_VITALS_PAGE_LOCATORS.stress_amount_dropdown_view,
                                    self.DAILY_VITALS_PAGE_LOCATORS.stress_amount_dropdown_options, 2)

        self.wait_for_visible(self.DAILY_VITALS_PAGE_LOCATORS.blood_pressure_input_field).clear()
        self.wait_for_visible(self.DAILY_VITALS_PAGE_LOCATORS.blood_pressure_input_field).send_keys(
            DailyVitals.blood_pressure)
        self.wait_for_visible(self.DAILY_VITALS_PAGE_LOCATORS.blood_pressure2_input_field).clear()
        self.wait_for_visible(self.DAILY_VITALS_PAGE_LOCATORS.blood_pressure2_input_field).send_keys(
            DailyVitals.blood_pressure1)
        self.click_when_ready(self.DAILY_VITALS_PAGE_LOCATORS.submit_add_vitals)
        self.make_pause(ThreedSleepValues.NORMAL_SLEEP)

        count = 0
        for link in self.get_elements(self.DAILY_VITALS_PAGE_LOCATORS.date_links):
            count += 1
            if DailyVitals.date in link.text:
                element = (By.CSS_SELECTOR, f".table-striped tr:nth-child({count}) td")
                column = self.get_elements(element)
                for webelement in column:
                    assert webelement.text.strip() != ""
                break
