from selenium.webdriver.common.by import By


class WorkoutCalcGeneralPageLocators:
    frame = (By.ID, "IntensityCalciFrame")
    submit_btn = (By.ID, "saveButtonSettings")
    results_in_tables = (By.XPATH, "//div[@class='w-box-content']/table")


class PalladinoWorkoutCalcPageLocators:
    palladino_title_text = (By.XPATH, "//h5[contains(.,'Calculate Interval Power Targets')]")
    palladino_btn = (By.XPATH, "//a[text()='Palladino']")
    critical_power_input_field = (By.ID, "CP")
    reserve_work_input_field = (By.ID, "RWC")
    short_test_input_field = (By.ID, "AVPWS")
    long_mm_input_field = (By.ID, "TimeMML")
    long_ss_input_field = (By.ID, "TimeSSL")
    long_test_input_field = (By.ID, "AVPWL")
    hh_input_field = (By.ID, "TimeHHR")
    mm_input_field = (By.ID, "TimeMMR")
    ss_input_field = (By.ID, "TimeSSR")
    race_avg_power_input_field = (By.ID, "RAP")
    rc_mm_input_field = (By.ID, "TimeMMRR")
    rc_ss_input_field = (By.ID, "TimeSSRR")
    race_avg_power_w_input_field = (By.ID, "RAPR")
    submit_btn1 = (By.ID, "saveButtonSettings2")
    submit_btn2 = (By.ID, "saveButtonSettings3")
    submit_btn3 = (By.ID, "saveButtonSettings4")


class TinmanWorkoutCalcPageLocators:
    tinman_title_text = (By.XPATH, "//h5[contains(.,'Enter your most recent Race Time')]")
    tinman_btn = (By.XPATH, "//a[text()='Tinman']")
    r_distance_dropdown = (By.XPATH, "//select[@name='distance']")
    r_distance_dropdown_view = (By.XPATH, "//select[@name='distance']/option")
    r_distance_dropdown_option = (By.XPATH, "//select[@name='distance']/option")
    male_radio_btn = (By.ID, "Male")


class McMillanWorkoutCalcPageLocators:
    mcmillan_title_text = (By.XPATH, "//h5[contains(.,'Enter a recent race time (or estimated time)')]")
    mcmillan_btn = (By.XPATH, "//a[text()='McMillan']")
    g_event_hh_input_field = (By.ID, "GTimeHH")
    g_event_mm_input_field = (By.ID, "GTimeMM")
    g_event_ss_input_field = (By.ID, "GTimeSS")
    race_distance_dropdown = (By.ID, "distance")
    race_distance_dropdown_view = (By.CSS_SELECTOR, "#distance option")
    race_distance_dropdown_option = (By.CSS_SELECTOR, "#distance option")
    goal_distance_dropdown = (By.XPATH, "//select[@name='goaldistance']")
    goal_distance_dropdown_view = (By.XPATH, "//select[@name='goaldistance']/option")
    goal_distance_dropdown_option = (By.XPATH, "//select[@name='goaldistance']/option")


class HansonWorkoutCalcPageLocators:
    hansons_title_text = (By.XPATH, "//h5[contains(.,'Enter a recent race time or goal time below')]")
    hansons_btn = (By.XPATH, "//a[text()='Hansons']")
    distance_dropdown = (By.ID, "RaceDist")
    distance_dropdown_view = (By.CSS_SELECTOR, "#RaceDist option")
    distance_dropdown_option = (By.CSS_SELECTOR, "#RaceDist option")
    temp_input_field = (By.ID, "Temp")
    humidity_input_field = (By.ID, "Humid")
    wind_speed_input_field = (By.ID, "Wind")


class IntensityHansonWorkoutCalcPageLocators:
    intensity_title_text = (By.XPATH, "//h4[contains(.,'Running Workout Intensity Calculator')]")
    intensity_btn = (By.XPATH, "//button[text()='Intensity']")
    event_radio_btn = (By.ID, "MARATHON")
    event_hh_input_field = (By.ID, "TimeHH")
    event_mm_input_field = (By.ID, "TimeMM")
    event_ss_input_field = (By.ID, "TimeSS")
