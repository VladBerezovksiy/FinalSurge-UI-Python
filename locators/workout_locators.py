from selenium.webdriver.common.by import By


class WorkoutGeneralPageLocators:
    options_table = (By.CSS_SELECTOR, ".w-box-header h4")


class NewActivityTypeWorkoutPageLocators:
    activity_type_input_field = (By.ID, "ATypeName")
    activity_type = (By.CSS_SELECTOR, "div.hideable .w-box-header h4")


class NewActivityZoneWorkoutPageLocators:
    zone_type_dropdown = (By.ID, "ZoneType")
    zone_type_dropdown_view = (By.CSS_SELECTOR, "#ZoneType option")
    zone_type_dropdown_options = (By.CSS_SELECTOR, "#ZoneType option")
    zone1_input_field = (By.ID, "Zone1High")
    zone2_input_field = (By.ID, "Zone2High")
    zone3_input_field = (By.ID, "Zone3High")
    zone4_input_field = (By.ID, "Zone4High")
    zone5_input_field = (By.ID, "Zone5High")
    zone6_input_field = (By.ID, "Zone6High")


class WorkoutLibraryWorkoutPageLocators:
    library_dropdown = (By.ID, "FolderID")
    library_code_input_field = (By.ID, "LibCode")
    plus_icon = (By.CSS_SELECTOR, ".icon-plus")
    table_new_activity_zone = (By.CSS_SELECTOR, ".table-condensed")
    library_table = (By.CSS_SELECTOR, ".table-condensed tr td:nth-child(2)")


class PrintWorkoutWorkoutPageLocators:
    print_link = (By.XPATH, "//table//a")
    print_result = (By.ID, "EditProfile")  # List of elements
    print_frame = (By.ID, "PrintWorkoutsiFrame")
    print_start_date_input = (By.ID, "PrintStartDate")
    print_end_date_input = (By.ID, "PrintEndDate")
    submit_print_btn = (By.ID, "saveButtonPrint")


class ReportAndStatisticsWorkoutPageLocators:
    end_date_input_field = (By.ID, "WorkoutDateEnd")
    list_view_radio_btn = (By.ID, "groupBy1")
    report_table = (By.CSS_SELECTOR, ".table-striped tr td:nth-child(2)")


class ViewCalendarWorkoutPageLocators:
    data_in_calendar = (By.CSS_SELECTOR, ".detailslink")  # List of elements
    quick_add_button = (By.ID, "QuickAddToggle")
    add_workout_library_button = (By.ID, "WorkoutLibAdd")
    full_add_button = (By.ID, "FullAddBtn")
    add_garmin_button = (By.ID, "GarminAddBtn")
    activity_type_dropdown = (By.ID, "ActivityType")
    activity_type_dropdown_view = (By.CSS_SELECTOR, "#ActivityType option")
    activity_type_dropdown_options = (By.CSS_SELECTOR, "#ActivityType option")
    how_i_feel_dropdown = (By.ID, "HowFeel")
    how_i_feel_dropdown_view = (By.CSS_SELECTOR, "#HowFeel option")
    how_i_feel_dropdown_options = (By.CSS_SELECTOR, "#HowFeel option")


class AddWorkoutWorkoutPageLocators:
    workout_form = (By.CSS_SELECTOR, "#col1 .w-box-content")
    date_input_field = (By.ID, "WorkoutDate")
    time_of_day_input_field = (By.ID, "WorkoutTime")
    workout_name_input_field = (By.ID, "Name")
    workout_description_input_field = (By.ID, "Desc")
    distance_checkbox = (By.ID, "PlannedWorkout")
    basic_workout_tab = (By.XPATH, "//*[@id='tBasic']/parent::li")
    distance_input_field = (By.ID, "Distance")
    distance_dropdown = (By.ID, "DistType")
    distance_dropdown_view = (By.CSS_SELECTOR, "#DistType option")
    distance_dropdown_options = (By.CSS_SELECTOR, "#DistType option")
    duration_input_field = (By.ID, "Duration")
    pace_input_field = (By.ID, "Pace")
    pace_dropdown = (By.ID, "PaceType")
    pace_dropdown_view = (By.CSS_SELECTOR, "#PaceType option")
    pace_dropdown_options = (By.CSS_SELECTOR, "#PaceType option")
    race_checkbox = (By.ID, "IsRace")
    place_input_field = (By.ID, "OverallPlace")
    age_group_place_input_field = (By.ID, "AgeGroupPlace")
    how_i_felt_radio_button = (By.ID, "hf_great")
    perceived_effort_dropdown = (By.ID, "PerEffort")
    perceived_effort_dropdown_view = (By.CSS_SELECTOR, "#PerEffort option")
    perceived_effort_dropdown_option = (By.CSS_SELECTOR, "#PerEffort option")
    add_workout_submit_btn = (By.ID, "saveButton")
    add_workout_submit_btn_locator = By.ID("saveButton")


class RunNavigationBarWorkoutPageLocators:
    run_tab = (By.XPATH, "//div[@id='blog_accordion_left']//div[@class='accordion-group'][1]")
    fartlek_sub_tab = (By.XPATH, "//div[@id='blog_accordion_left']//div[@class='accordion-group'][1]/div[@id]//li[2]/a")
    hills_sub_tab = (By.XPATH, "//div[@id='blog_accordion_left']//div[@class='accordion-group'][1]/div[@id]//li[3]/a")
