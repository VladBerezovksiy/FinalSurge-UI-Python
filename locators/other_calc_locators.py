from selenium.webdriver.common.by import By


class OtherCalcGeneralPageLocators:
    frame = (By.ID, "OtherCalciFrame")
    submit_btn = (By.ID, "saveButtonSettings")
    results_in_tables = (By.XPATH, "//div[@class='w-box-content']/table")


class CalculatorPageLocators:
    pace_calc_tab = (By.XPATH, "//a[text()='Pace Calculator']")
    pace_calc_tab_locator = By.XPATH("//a[text()='Pace Calculator']")
    pace_calc_title_text = (By.XPATH, "//h5[contains(.,'Enter a distance and time to calculate pace:')]")
    distance_input_field = (By.ID, "RunDist")
    distance_dropdown = (By.ID, "RaceDist")
    distance_dropdown_view = (By.CSS_SELECTOR, "#RaceDist option")
    distance_dropdown_options = (By.CSS_SELECTOR, "#RaceDist option")
    hh_input_field = (By.ID, "TimeHH")
    mm_input_field = (By.ID, "TimeMM")
    ss_input_field = (By.ID, "TimeSS")


class CaloricPageLocators:
    caloric_needs_tab = (By.XPATH, "//a[text()='Caloric Needs']")
    caloric_needs_title_text = (By.XPATH, "//h5[contains(.,'Enter your information below:')]")
    weight_input_field = (By.ID, "Weight")
    height_input_field = (By.ID, "HeightInchCent")
    age_input_field = (By.ID, "Age")
    run_distance_input_field = (By.ID, "RunDist")
    male_radio_button = (By.ID, "optionsRadios5")
