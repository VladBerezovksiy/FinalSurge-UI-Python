import allure

from base.base_page import BasePage
from locators.workout_calc_locators import WorkoutCalcGeneralPageLocators, PalladinoWorkoutCalcPageLocators, \
    TinmanWorkoutCalcPageLocators, McMillanWorkoutCalcPageLocators, HansonWorkoutCalcPageLocators, \
    IntensityHansonWorkoutCalcPageLocators
from models.WorkoutCalcModel import WorkoutCalc
from utils.constants import ThreedSleepValues


class WorkoutCalcPage(BasePage):
    WORKOUT_CALC_GENERAL_PAGE_LOCATORS = WorkoutCalcGeneralPageLocators()
    PALLADINO_WORKOUT_PAGE_LOCATORS = PalladinoWorkoutCalcPageLocators()
    TINMAN_WORKOUT_PAGE_LOCATORS = TinmanWorkoutCalcPageLocators()
    MCMILLAN_WORKOUT_PAGE_LOCATORS = McMillanWorkoutCalcPageLocators()
    HANSON_WORKOUT_PAGE_LOCATORS = HansonWorkoutCalcPageLocators()
    INTENSITY_HANSON_WORKOUT_PAGE_LOCATORS = IntensityHansonWorkoutCalcPageLocators()

    @allure.step("Add Intensity in Workout Calc")
    def add_intensity(self):
        self.login(self.cred.LOGIN, self.cred.PASSWORD)
        self.click_when_ready(self.TOP_NAVIG_BAR_LOCATORS.workout_calculator_icon)
        self.wait_js_is_loaded()
        self.switch_to_frame(self.WORKOUT_CALC_GENERAL_PAGE_LOCATORS.frame)
        self.click_when_ready(self.INTENSITY_HANSON_WORKOUT_PAGE_LOCATORS.intensity_btn)
        self.wait_for_visible(self.INTENSITY_HANSON_WORKOUT_PAGE_LOCATORS.intensity_title_text)
        self.click_when_ready(self.INTENSITY_HANSON_WORKOUT_PAGE_LOCATORS.event_radio_btn)
        self.wait_for_visible(self.INTENSITY_HANSON_WORKOUT_PAGE_LOCATORS.event_hh_input_field).clear()
        self.wait_for_visible(self.INTENSITY_HANSON_WORKOUT_PAGE_LOCATORS.event_hh_input_field).send_keys(
            WorkoutCalc.recent_hh)
        self.wait_for_visible(self.INTENSITY_HANSON_WORKOUT_PAGE_LOCATORS.event_mm_input_field).clear()
        self.wait_for_visible(self.INTENSITY_HANSON_WORKOUT_PAGE_LOCATORS.event_mm_input_field).send_keys(
            WorkoutCalc.recent_mm)
        self.wait_for_visible(self.INTENSITY_HANSON_WORKOUT_PAGE_LOCATORS.event_ss_input_field).clear()
        self.wait_for_visible(self.INTENSITY_HANSON_WORKOUT_PAGE_LOCATORS.event_ss_input_field).send_keys(
            WorkoutCalc.recent_ss)
        self.click_when_ready(self.WORKOUT_CALC_GENERAL_PAGE_LOCATORS.submit_btn)
        self.make_pause(ThreedSleepValues.NORMAL_SLEEP)
        assert self.get_element(self.WORKOUT_CALC_GENERAL_PAGE_LOCATORS.results_in_tables).is_displayed()

    @allure.step("Add Hansons in Workout Calc")
    def add_hansons(self):
        self.login(self.cred.LOGIN, self.cred.PASSWORD)
        self.click_when_ready(self.TOP_NAVIG_BAR_LOCATORS.workout_calculator_icon)
        self.wait_js_is_loaded()
        self.switch_to_frame(self.WORKOUT_CALC_GENERAL_PAGE_LOCATORS.frame)
        self.click_when_ready(self.HANSON_WORKOUT_PAGE_LOCATORS.hansons_btn)
        self.wait_for_visible(self.HANSON_WORKOUT_PAGE_LOCATORS.hansons_title_text)
        self.select_dropdown_option(self.HANSON_WORKOUT_PAGE_LOCATORS.distance_dropdown,
                                    self.HANSON_WORKOUT_PAGE_LOCATORS.distance_dropdown_view,
                                    self.HANSON_WORKOUT_PAGE_LOCATORS.distance_dropdown_option, 1)
        self.wait_for_visible(self.INTENSITY_HANSON_WORKOUT_PAGE_LOCATORS.event_hh_input_field).clear()
        self.wait_for_visible(self.INTENSITY_HANSON_WORKOUT_PAGE_LOCATORS.event_hh_input_field).send_keys(
            WorkoutCalc.recent_hh)
        self.wait_for_visible(self.INTENSITY_HANSON_WORKOUT_PAGE_LOCATORS.event_mm_input_field).clear()
        self.wait_for_visible(self.INTENSITY_HANSON_WORKOUT_PAGE_LOCATORS.event_mm_input_field).send_keys(
            WorkoutCalc.recent_mm)
        self.wait_for_visible(self.INTENSITY_HANSON_WORKOUT_PAGE_LOCATORS.event_ss_input_field).clear()
        self.wait_for_visible(self.INTENSITY_HANSON_WORKOUT_PAGE_LOCATORS.event_ss_input_field).send_keys(
            WorkoutCalc.recent_ss)
        self.wait_for_visible(self.HANSON_WORKOUT_PAGE_LOCATORS.temp_input_field).clear()
        self.wait_for_visible(self.HANSON_WORKOUT_PAGE_LOCATORS.temp_input_field).send_keys(
            WorkoutCalc.temperature)
        self.wait_for_visible(self.HANSON_WORKOUT_PAGE_LOCATORS.humidity_input_field).clear()
        self.wait_for_visible(self.HANSON_WORKOUT_PAGE_LOCATORS.humidity_input_field).send_keys(
            WorkoutCalc.humidity)
        self.wait_for_visible(self.HANSON_WORKOUT_PAGE_LOCATORS.wind_speed_input_field).clear()
        self.wait_for_visible(self.HANSON_WORKOUT_PAGE_LOCATORS.wind_speed_input_field).send_keys(
            WorkoutCalc.wind_speed)
        self.click_when_ready(self.WORKOUT_CALC_GENERAL_PAGE_LOCATORS.submit_btn)
        self.make_pause(ThreedSleepValues.NORMAL_SLEEP)
        assert self.get_element(self.WORKOUT_CALC_GENERAL_PAGE_LOCATORS.results_in_tables).is_displayed()

    @allure.step("Add McMillan in Workout Calc")
    def add_mcmillan(self):
        self.login(self.cred.LOGIN, self.cred.PASSWORD)
        self.click_when_ready(self.TOP_NAVIG_BAR_LOCATORS.workout_calculator_icon)
        self.wait_js_is_loaded()
        self.switch_to_frame(self.WORKOUT_CALC_GENERAL_PAGE_LOCATORS.frame)
        self.click_when_ready(self.MCMILLAN_WORKOUT_PAGE_LOCATORS.mcmillan_btn)
        self.wait_for_visible(self.MCMILLAN_WORKOUT_PAGE_LOCATORS.mcmillan_title_text)
        self.select_dropdown_option(self.MCMILLAN_WORKOUT_PAGE_LOCATORS.race_distance_dropdown,
                                    self.MCMILLAN_WORKOUT_PAGE_LOCATORS.race_distance_dropdown_view,
                                    self.MCMILLAN_WORKOUT_PAGE_LOCATORS.race_distance_dropdown_option, 27)
        self.wait_for_visible(self.INTENSITY_HANSON_WORKOUT_PAGE_LOCATORS.event_hh_input_field).clear()
        self.wait_for_visible(self.INTENSITY_HANSON_WORKOUT_PAGE_LOCATORS.event_hh_input_field).send_keys(
            WorkoutCalc.recent_hh)
        self.wait_for_visible(self.INTENSITY_HANSON_WORKOUT_PAGE_LOCATORS.event_mm_input_field).clear()
        self.wait_for_visible(self.INTENSITY_HANSON_WORKOUT_PAGE_LOCATORS.event_mm_input_field).send_keys(
            WorkoutCalc.recent_mm)
        self.wait_for_visible(self.INTENSITY_HANSON_WORKOUT_PAGE_LOCATORS.event_ss_input_field).clear()
        self.wait_for_visible(self.INTENSITY_HANSON_WORKOUT_PAGE_LOCATORS.event_ss_input_field).send_keys(
            WorkoutCalc.recent_ss)
        self.select_dropdown_option(self.MCMILLAN_WORKOUT_PAGE_LOCATORS.goal_distance_dropdown,
                                    self.MCMILLAN_WORKOUT_PAGE_LOCATORS.goal_distance_dropdown_view,
                                    self.MCMILLAN_WORKOUT_PAGE_LOCATORS.goal_distance_dropdown_option, 29)
        self.wait_for_visible(self.MCMILLAN_WORKOUT_PAGE_LOCATORS.g_event_hh_input_field).clear()
        self.wait_for_visible(self.MCMILLAN_WORKOUT_PAGE_LOCATORS.g_event_hh_input_field).send_keys(
            WorkoutCalc.goal_hh)
        self.wait_for_visible(self.MCMILLAN_WORKOUT_PAGE_LOCATORS.g_event_mm_input_field).clear()
        self.wait_for_visible(self.MCMILLAN_WORKOUT_PAGE_LOCATORS.g_event_mm_input_field).send_keys(
            WorkoutCalc.goal_mm)
        self.wait_for_visible(self.MCMILLAN_WORKOUT_PAGE_LOCATORS.g_event_ss_input_field).clear()
        self.wait_for_visible(self.MCMILLAN_WORKOUT_PAGE_LOCATORS.g_event_ss_input_field).send_keys(
            WorkoutCalc.goal_ss)
        self.click_when_ready(self.WORKOUT_CALC_GENERAL_PAGE_LOCATORS.submit_btn)
        self.make_pause(ThreedSleepValues.NORMAL_SLEEP)
        assert self.get_element(self.WORKOUT_CALC_GENERAL_PAGE_LOCATORS.results_in_tables).is_displayed()

    @allure.step("Add Tinman in Workout Calc")
    def add_tinman(self):
        self.login(self.cred.LOGIN, self.cred.PASSWORD)
        self.click_when_ready(self.TOP_NAVIG_BAR_LOCATORS.workout_calculator_icon)
        self.wait_js_is_loaded()
        self.switch_to_frame(self.WORKOUT_CALC_GENERAL_PAGE_LOCATORS.frame)
        self.click_when_ready(self.TINMAN_WORKOUT_PAGE_LOCATORS.tinman_btn)
        self.wait_for_visible(self.TINMAN_WORKOUT_PAGE_LOCATORS.tinman_title_text)
        self.select_dropdown_option(self.TINMAN_WORKOUT_PAGE_LOCATORS.r_distance_dropdown,
                                    self.TINMAN_WORKOUT_PAGE_LOCATORS.r_distance_dropdown_view,
                                    self.TINMAN_WORKOUT_PAGE_LOCATORS.r_distance_dropdown_option, 27)
        self.wait_for_visible(self.INTENSITY_HANSON_WORKOUT_PAGE_LOCATORS.event_hh_input_field).clear()
        self.wait_for_visible(self.INTENSITY_HANSON_WORKOUT_PAGE_LOCATORS.event_hh_input_field).send_keys(
            WorkoutCalc.recent_hh)
        self.wait_for_visible(self.INTENSITY_HANSON_WORKOUT_PAGE_LOCATORS.event_mm_input_field).clear()
        self.wait_for_visible(self.INTENSITY_HANSON_WORKOUT_PAGE_LOCATORS.event_mm_input_field).send_keys(
            WorkoutCalc.recent_mm)
        self.wait_for_visible(self.INTENSITY_HANSON_WORKOUT_PAGE_LOCATORS.event_ss_input_field).clear()
        self.wait_for_visible(self.INTENSITY_HANSON_WORKOUT_PAGE_LOCATORS.event_ss_input_field).send_keys(
            WorkoutCalc.recent_ss)
        self.click_when_ready(self.TINMAN_WORKOUT_PAGE_LOCATORS.male_radio_btn)
        self.click_when_ready(self.WORKOUT_CALC_GENERAL_PAGE_LOCATORS.submit_btn)
        self.make_pause(ThreedSleepValues.NORMAL_SLEEP)
        assert self.get_element(self.WORKOUT_CALC_GENERAL_PAGE_LOCATORS.results_in_tables).is_displayed()

    @allure.step("Add Palladino in Workout Calc")
    def add_palladino(self):
        self.login(self.cred.LOGIN, self.cred.PASSWORD)
        self.click_when_ready(self.TOP_NAVIG_BAR_LOCATORS.workout_calculator_icon)
        self.wait_js_is_loaded()
        self.switch_to_frame(self.WORKOUT_CALC_GENERAL_PAGE_LOCATORS.frame)
        self.click_when_ready(self.PALLADINO_WORKOUT_PAGE_LOCATORS.palladino_btn)
        self.wait_for_visible(self.PALLADINO_WORKOUT_PAGE_LOCATORS.palladino_title_text)
        self.wait_for_visible(self.PALLADINO_WORKOUT_PAGE_LOCATORS.critical_power_input_field).clear()
        self.wait_for_visible(self.PALLADINO_WORKOUT_PAGE_LOCATORS.critical_power_input_field).send_keys(
            WorkoutCalc.critical_power)
        self.wait_for_visible(self.PALLADINO_WORKOUT_PAGE_LOCATORS.reserve_work_input_field).clear()
        self.wait_for_visible(self.PALLADINO_WORKOUT_PAGE_LOCATORS.reserve_work_input_field).send_keys(
            WorkoutCalc.reserve_work_capacity)
        self.click_when_ready(self.WORKOUT_CALC_GENERAL_PAGE_LOCATORS.submit_btn)
        self.make_pause(ThreedSleepValues.NORMAL_SLEEP)
        assert self.get_element(self.WORKOUT_CALC_GENERAL_PAGE_LOCATORS.results_in_tables).is_displayed()

        self.wait_for_visible(self.INTENSITY_HANSON_WORKOUT_PAGE_LOCATORS.event_mm_input_field).clear()
        self.wait_for_visible(self.INTENSITY_HANSON_WORKOUT_PAGE_LOCATORS.event_mm_input_field).send_keys(
            WorkoutCalc.recent_mm)
        self.wait_for_visible(self.INTENSITY_HANSON_WORKOUT_PAGE_LOCATORS.event_ss_input_field).clear()
        self.wait_for_visible(self.INTENSITY_HANSON_WORKOUT_PAGE_LOCATORS.event_ss_input_field).send_keys(
            WorkoutCalc.recent_ss)
        self.wait_for_visible(self.PALLADINO_WORKOUT_PAGE_LOCATORS.short_test_input_field).clear()
        self.wait_for_visible(self.PALLADINO_WORKOUT_PAGE_LOCATORS.short_test_input_field).send_keys(
            WorkoutCalc.short_test)

        self.wait_for_visible(self.PALLADINO_WORKOUT_PAGE_LOCATORS.long_mm_input_field).clear()
        self.wait_for_visible(self.PALLADINO_WORKOUT_PAGE_LOCATORS.long_mm_input_field).send_keys(
            WorkoutCalc.goal_mm)
        self.wait_for_visible(self.PALLADINO_WORKOUT_PAGE_LOCATORS.long_ss_input_field).clear()
        self.wait_for_visible(self.PALLADINO_WORKOUT_PAGE_LOCATORS.long_ss_input_field).send_keys(
            WorkoutCalc.goal_ss)
        self.wait_for_visible(self.PALLADINO_WORKOUT_PAGE_LOCATORS.long_test_input_field).clear()
        self.wait_for_visible(self.PALLADINO_WORKOUT_PAGE_LOCATORS.long_test_input_field).send_keys(
            WorkoutCalc.long_test)
        self.click_when_ready(self.WORKOUT_CALC_GENERAL_PAGE_LOCATORS.submit_btn)
        self.make_pause(ThreedSleepValues.NORMAL_SLEEP)
        assert self.get_element(self.WORKOUT_CALC_GENERAL_PAGE_LOCATORS.results_in_tables).is_displayed()

        self.wait_for_visible(self.PALLADINO_WORKOUT_PAGE_LOCATORS.hh_input_field).clear()
        self.wait_for_visible(self.PALLADINO_WORKOUT_PAGE_LOCATORS.hh_input_field).send_keys(
            WorkoutCalc.goal_hh)
        self.wait_for_visible(self.PALLADINO_WORKOUT_PAGE_LOCATORS.mm_input_field).clear()
        self.wait_for_visible(self.PALLADINO_WORKOUT_PAGE_LOCATORS.mm_input_field).send_keys(
            WorkoutCalc.goal_mm)
        self.wait_for_visible(self.PALLADINO_WORKOUT_PAGE_LOCATORS.ss_input_field).clear()
        self.wait_for_visible(self.PALLADINO_WORKOUT_PAGE_LOCATORS.ss_input_field).send_keys(
            WorkoutCalc.goal_ss)
        self.wait_for_visible(self.PALLADINO_WORKOUT_PAGE_LOCATORS.race_avg_power_input_field).clear()
        self.wait_for_visible(self.PALLADINO_WORKOUT_PAGE_LOCATORS.race_avg_power_input_field).send_keys(
            WorkoutCalc.race_avg_power_w)
        self.click_when_ready(self.WORKOUT_CALC_GENERAL_PAGE_LOCATORS.submit_btn)
        self.make_pause(ThreedSleepValues.NORMAL_SLEEP)
        assert self.get_element(self.WORKOUT_CALC_GENERAL_PAGE_LOCATORS.results_in_tables).is_displayed()

        self.wait_for_visible(self.PALLADINO_WORKOUT_PAGE_LOCATORS.rc_mm_input_field).clear()
        self.wait_for_visible(self.PALLADINO_WORKOUT_PAGE_LOCATORS.rc_mm_input_field).send_keys(
            WorkoutCalc.recent_mm)
        self.wait_for_visible(self.PALLADINO_WORKOUT_PAGE_LOCATORS.rc_ss_input_field).clear()
        self.wait_for_visible(self.PALLADINO_WORKOUT_PAGE_LOCATORS.rc_ss_input_field).send_keys(
            WorkoutCalc.recent_ss)
        self.wait_for_visible(self.PALLADINO_WORKOUT_PAGE_LOCATORS.race_avg_power_w_input_field).clear()
        self.wait_for_visible(self.PALLADINO_WORKOUT_PAGE_LOCATORS.race_avg_power_w_input_field).send_keys(
            WorkoutCalc.race_avg_power_w)
        self.click_when_ready(self.WORKOUT_CALC_GENERAL_PAGE_LOCATORS.submit_btn)
        self.make_pause(ThreedSleepValues.NORMAL_SLEEP)
        assert self.get_element(self.WORKOUT_CALC_GENERAL_PAGE_LOCATORS.results_in_tables).is_displayed()
