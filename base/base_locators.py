from selenium.webdriver.common.by import By


class LoginLocators:
    login_panel = (By.ID, "login-position")
    logout_panel = (By.ID, "login-wrapper")
    email_input_field = (By.ID, "login_name")
    password_input_field = (By.ID, "login_password")
    login_button = (By.CSS_SELECTOR, "#login-validate button")
    account_login_button = (By.CSS_SELECTOR, "#login-wrapper .signup a")
    forgot_password_button = (By.ID, "pass_login")


class UserNavigateBarLocators:
    settings_link = (By.CSS_SELECTOR, ".user-box-inner .unstyled li:nth-child(1)")
    logout_link = (By.CSS_SELECTOR, ".user-box-inner .unstyled li:nth-child(3)")


class TopNavigationBarLocators:
    dashboard_icon = (By.CSS_SELECTOR, ".nav-icons li:nth-child(1) a")
    calendar_icon = (By.CSS_SELECTOR, ".nav-icons li:nth-child(2) a")
    workout_calculator_icon = (By.CSS_SELECTOR, ".nav-icons li:nth-child(3) a")
    other_calculator_icon = (By.CSS_SELECTOR, ".nav-icons li:nth-child(4) a")
    reports_statistics_icon = (By.CSS_SELECTOR, ".nav-icons li:nth-child(5) a")
    mail_box_icon = (By.CSS_SELECTOR, ".nav-icons li:nth-child(6) a")
    print_workouts_icon = (By.CSS_SELECTOR, ".nav-icons li:nth-child(7) a")
    beta_platforms_icon = (By.CSS_SELECTOR, ".nav-icons li:nth-child(8) a")


class WorkoutListLocators:
    workout_btn = (By.XPATH, "//ul[@id='mobile-nav']/li[1]/a")
    add_workout_btn = (By.XPATH, "//ul[@id='mobile-nav']/li[1]/ul/li[1]/a")
    garmin_btn = (By.XPATH, "//ul[@id='mobile-nav']/li[1]/ul/li[2]/a")
    view_calendar_btn = (By.XPATH, "//ul[@id='mobile-nav']/li[1]/ul/li[3]/a")
    reports_statistics_btn = (By.XPATH, "//ul[@id='mobile-nav']/li[1]/ul/li[4]/a")
    print_workout_btn = (By.XPATH, "//ul[@id='mobile-nav']/li[1]/ul/li[5]/a")
    workout_library_btn = (By.XPATH, "//ul[@id='mobile-nav']/li[1]/ul/li[6]/a")
    hr_zones_btn = (By.XPATH, "//ul[@id='mobile-nav']/li[1]/ul/li[7]/a")
    customize_activity_btn = (By.XPATH, "//ul[@id='mobile-nav']/li[1]/ul/li[8]/a")
    import_data_btn = (By.XPATH, "//ul[@id='mobile-nav']/li[1]/ul/li[9]/a")


class DailyVitalsLocators:
    daily_vitals_btn = (By.XPATH, "//ul[@id='mobile-nav']/li[2]/a")
    view_add_vitals_btn = (By.XPATH, "//ul[@id='mobile-nav']/li[2]/ul/li[1]/a")


class GearRoutesLocators:
    gear_routes_btn = (By.XPATH, "//ul[@id='mobile-nav']/li[3]/a")
    shoes_btn = (By.XPATH, "//ul[@id='mobile-nav']/li[3]/ul/li[1]/a")
    bikes_btn = (By.XPATH, "//ul[@id='mobile-nav']/li[3]/ul/li[2]/a")
    routes_btn = (By.XPATH, "//ul[@id='mobile-nav']/li[3]/ul/li[3]/a")


class TrainingLocators:
    training_plans_btn = (By.XPATH, "//ul[@id='mobile-nav']/li[4]/a")
    view_my_plans_btn = (By.XPATH, "//ul[@id='mobile-nav']/li[4]/ul/li[1]/a")
    find_my_plans_btn = (By.XPATH, "//ul[@id='mobile-nav']/li[4]/ul/li[2]/a")


class ResourcesLocators:
    resources_btn = (By.XPATH, "//ul[@id='mobile-nav']/li[5]/a")
    view_files_resources_btn = (By.XPATH, "//ul[@id='mobile-nav']/li[5]/ul/li[1]/a")


class MessageBoardsLocators:
    message_boards_btn = (By.XPATH, "//ul[@id='mobile-nav']/li[6]/a")
    view_boards_btn = (By.XPATH, "//ul[@id='mobile-nav']/li[6]/ul/li[1]/a")
