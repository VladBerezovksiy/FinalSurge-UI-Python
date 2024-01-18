import allure

from base.base_page import BasePage
from locators.gear_routes_locators import GearRoutesGeneralPageLocators, RoutesPageLocators, BikesPageLocators, \
    ShoesPageLocators
from models.ShoesModel import Shoes
from models.BikesModel import Bikes
from models.RoutesModel import Routes
from utils.constants import ThreedSleepValues


class GearRoutesPage(BasePage):
    GEAR_ROUTES_GENERAL_PAGE_LOCATORS = GearRoutesGeneralPageLocators()
    ROUTS_PAGE_LOCATORS = RoutesPageLocators()
    BIKES_PAGE_LOCATORS = BikesPageLocators()
    SHOES_PAGE_LOCATORS = ShoesPageLocators()

    @allure.step("Add Shoe")
    def add_shoes(self):
        self.login(self.cred.LOGIN, self.cred.PASSWORD)
        self.hover_over_element(self.GEAR_ROUTES_LOCATORS.gear_routes_btn)
        self.click_when_ready(self.GEAR_ROUTES_LOCATORS.shoes_btn)
        self.wait_for_visible(self.SHOES_PAGE_LOCATORS.shoe_form)
        self.wait_for_visible(self.GEAR_ROUTES_GENERAL_PAGE_LOCATORS.name_input_field).clear()
        self.wait_for_visible(self.GEAR_ROUTES_GENERAL_PAGE_LOCATORS.name_input_field).send_keys(Shoes.name)
        self.select_dropdown_option(self.GEAR_ROUTES_GENERAL_PAGE_LOCATORS.brand_dropdown,
                                    self.GEAR_ROUTES_GENERAL_PAGE_LOCATORS.brand_dropdown_view,
                                    self.GEAR_ROUTES_GENERAL_PAGE_LOCATORS.brand_dropdown_options, 3)
        self.wait_for_visible(self.GEAR_ROUTES_GENERAL_PAGE_LOCATORS.model_input_field).clear()
        self.wait_for_visible(self.GEAR_ROUTES_GENERAL_PAGE_LOCATORS.model_input_field).send_keys(Shoes.modal)
        self.wait_for_visible(self.GEAR_ROUTES_GENERAL_PAGE_LOCATORS.cost_input_field).clear()
        self.wait_for_visible(self.GEAR_ROUTES_GENERAL_PAGE_LOCATORS.cost_input_field).send_keys(Shoes.cost)
        self.select_dropdown_option(self.SHOES_PAGE_LOCATORS.shoe_size_dropdown,
                                    self.SHOES_PAGE_LOCATORS.shoe_size_dropdown_view,
                                    self.SHOES_PAGE_LOCATORS.shoe_size_dropdown_options, 4)
        self.wait_for_visible(self.GEAR_ROUTES_GENERAL_PAGE_LOCATORS.dist_start_input_field).clear()
        self.wait_for_visible(self.GEAR_ROUTES_GENERAL_PAGE_LOCATORS.dist_start_input_field).send_keys(
            Shoes.starting_distance)
        self.wait_for_visible(self.GEAR_ROUTES_GENERAL_PAGE_LOCATORS.dist_alert_input_field).clear()
        self.wait_for_visible(self.GEAR_ROUTES_GENERAL_PAGE_LOCATORS.dist_alert_input_field).send_keys(
            Shoes.distance_alert)
        self.wait_for_visible(self.GEAR_ROUTES_GENERAL_PAGE_LOCATORS.notes_input_field).clear()
        self.wait_for_visible(self.GEAR_ROUTES_GENERAL_PAGE_LOCATORS.notes_input_field).send_keys(
            Shoes.notes)
        self.click_when_ready(self.GEAR_ROUTES_GENERAL_PAGE_LOCATORS.submit_btn)
        self.make_pause(ThreedSleepValues.NORMAL_SLEEP)
        assert self.get_size(self.GEAR_ROUTES_GENERAL_PAGE_LOCATORS.table_results) != 0

    @allure.step("Add Bike")
    def add_bikes(self):
        self.login(self.cred.LOGIN, self.cred.PASSWORD)
        self.hover_over_element(self.GEAR_ROUTES_LOCATORS.gear_routes_btn)
        self.click_when_ready(self.GEAR_ROUTES_LOCATORS.bikes_btn)
        self.click_when_ready(self.BIKES_PAGE_LOCATORS.bike_form)
        self.wait_for_visible(self.GEAR_ROUTES_GENERAL_PAGE_LOCATORS.name_input_field).clear()
        self.wait_for_visible(self.GEAR_ROUTES_GENERAL_PAGE_LOCATORS.name_input_field).send_keys(Bikes.name)
        self.select_dropdown_option(self.GEAR_ROUTES_GENERAL_PAGE_LOCATORS.brand_dropdown,
                                    self.GEAR_ROUTES_GENERAL_PAGE_LOCATORS.brand_dropdown_view,
                                    self.GEAR_ROUTES_GENERAL_PAGE_LOCATORS.brand_dropdown_options, 3)
        self.wait_for_visible(self.GEAR_ROUTES_GENERAL_PAGE_LOCATORS.model_input_field).clear()
        self.wait_for_visible(self.GEAR_ROUTES_GENERAL_PAGE_LOCATORS.model_input_field).send_keys(Bikes.modal)
        self.wait_for_visible(self.GEAR_ROUTES_GENERAL_PAGE_LOCATORS.cost_input_field).clear()
        self.wait_for_visible(self.GEAR_ROUTES_GENERAL_PAGE_LOCATORS.cost_input_field).send_keys(Bikes.cost)
        self.wait_for_visible(self.GEAR_ROUTES_GENERAL_PAGE_LOCATORS.dist_start_input_field).clear()
        self.wait_for_visible(self.GEAR_ROUTES_GENERAL_PAGE_LOCATORS.dist_start_input_field).send_keys(
            Bikes.starting_distance)
        self.click_when_ready(self.BIKES_PAGE_LOCATORS.track_dist_checkbox)
        self.wait_for_visible(self.GEAR_ROUTES_GENERAL_PAGE_LOCATORS.dist_alert_input_field).clear()
        self.wait_for_visible(self.GEAR_ROUTES_GENERAL_PAGE_LOCATORS.dist_alert_input_field).send_keys(
            Bikes.distance_alert)
        self.wait_for_visible(self.GEAR_ROUTES_GENERAL_PAGE_LOCATORS.notes_input_field).clear()
        self.wait_for_visible(self.GEAR_ROUTES_GENERAL_PAGE_LOCATORS.notes_input_field).send_keys(
            Bikes.notes)
        self.click_when_ready(self.GEAR_ROUTES_GENERAL_PAGE_LOCATORS.submit_btn)
        self.make_pause(ThreedSleepValues.NORMAL_SLEEP)
        assert self.get_size(self.GEAR_ROUTES_GENERAL_PAGE_LOCATORS.table_results) != 0

    @allure.step("Add Route")
    def add_routes(self):
        self.login(self.cred.LOGIN, self.cred.PASSWORD)
        self.hover_over_element(self.GEAR_ROUTES_LOCATORS.gear_routes_btn)
        self.click_when_ready(self.GEAR_ROUTES_LOCATORS.routes_btn)
        self.click_when_ready(self.ROUTS_PAGE_LOCATORS.routes_form)
        self.wait_for_visible(self.ROUTS_PAGE_LOCATORS.routes_name_input_field).clear()
        self.wait_for_visible(self.ROUTS_PAGE_LOCATORS.routes_name_input_field).send_keys(Routes.name)
        self.select_dropdown_option(self.ROUTS_PAGE_LOCATORS.routes_activity_dropdown,
                                    self.ROUTS_PAGE_LOCATORS.routes_activity_dropdown_view,
                                    self.ROUTS_PAGE_LOCATORS.routes_activity_dropdown_options, 3)
        self.wait_for_visible(self.ROUTS_PAGE_LOCATORS.routes_distance_input_field).clear()
        self.wait_for_visible(self.ROUTS_PAGE_LOCATORS.routes_distance_input_field).send_keys(Routes.distance)
        self.wait_for_visible(self.ROUTS_PAGE_LOCATORS.routes_record_input_field).clear()
        self.wait_for_visible(self.ROUTS_PAGE_LOCATORS.routes_record_input_field).send_keys(Routes.route_record)
        self.wait_for_visible(self.ROUTS_PAGE_LOCATORS.routes_record_date_input_field).clear()
        self.wait_for_visible(self.ROUTS_PAGE_LOCATORS.routes_record_date_input_field).send_keys(
            Routes.date_record)
        self.wait_for_visible(self.ROUTS_PAGE_LOCATORS.routes_desc_input_field).clear()
        self.wait_for_visible(self.ROUTS_PAGE_LOCATORS.routes_desc_input_field).send_keys(
            Routes.notes)
        self.click_when_ready(self.GEAR_ROUTES_GENERAL_PAGE_LOCATORS.submit_btn)
        self.make_pause(ThreedSleepValues.NORMAL_SLEEP)
        assert self.get_size(self.GEAR_ROUTES_GENERAL_PAGE_LOCATORS.table_results) != 0
