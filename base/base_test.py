import pytest

from pages.daily_vitals_page import DailyVitalsPage
from pages.gear_routes_page import GearRoutesPage
from pages.login_page import LoginPage
from pages.mail_box_page import MailBoxPage
from pages.message_boards_page import MessageBoardsPage
from pages.other_calc_page import OtherCalcPage
from pages.resources_page import ResourcesPage
from pages.training_plans_page import TrainingPage
from pages.workout_calc_page import WorkoutCalcPage
from pages.workout_page import WorkoutPage
from utils.credential import CredData


class BaseTest:
    cred = CredData()

    login_page: LoginPage
    daily_vitals_page: DailyVitalsPage
    gear_routes_page: GearRoutesPage
    mail_box_page: MailBoxPage
    message_boards_page: MessageBoardsPage
    other_calc_page: OtherCalcPage
    resources_page: ResourcesPage
    training_page: TrainingPage
    workout_calc_page: WorkoutCalcPage
    workout_page: WorkoutPage

    @pytest.fixture(autouse=True)
    def setup(self, request, get_driver):
        request.cls.get_driver = get_driver

        request.cls.login_page = LoginPage(get_driver)
        request.cls.daily_vitals_page = DailyVitalsPage(get_driver)
        request.cls.gear_routes_page = GearRoutesPage(get_driver)
        request.cls.mail_box_page = MailBoxPage(get_driver)
        request.cls.message_boards_page = MessageBoardsPage(get_driver)
        request.cls.other_calc_page = OtherCalcPage(get_driver)
        request.cls.resources_page = ResourcesPage(get_driver)
        request.cls.training_page = TrainingPage(get_driver)
        request.cls.workout_calc_page = WorkoutCalcPage(get_driver)
        request.cls.workout_page = WorkoutPage(get_driver)
