from selenium.webdriver.common.by import By


class GearRoutesGeneralPageLocators:
    edit_btn = (By.XPATH, "//a[@title='Edit']")
    trash_btn = (By.XPATH, "//table//a[@title='Delete']")
    ok_btn = (By.XPATH, "//div[@class='modal-footer']/a[contains(.,'OK')]")
    submit_btn = (By.ID, "saveButton")
    table_results = (By.CSS_SELECTOR, ".w-box-content tr td:nth-child(2)")
    name_input_field = (By.ID, "ShoeName")
    model_input_field = (By.ID, "ShoeModel")
    cost_input_field = (By.ID, "ShoeCost")
    dist_start_input_field = (By.ID, "StartDist")
    dist_alert_input_field = (By.ID, "DistAlert")
    notes_input_field = (By.ID, "ShoeNotes")
    brand_dropdown = (By.CSS_SELECTOR, "#s2id_ShoeBrand a")
    brand_dropdown_view = (By.CSS_SELECTOR, ".select2-results")
    brand_dropdown_options = (By.CSS_SELECTOR, ".select2-results li")


class RoutesPageLocators:
    routes_form = (By.ID, "RouteBox")
    routes_name_input_field = (By.ID, "RouteName")
    routes_activity_dropdown = (By.ID, "Activity")
    routes_activity_dropdown_view = (By.CSS_SELECTOR, "#Activity option")
    routes_activity_dropdown_options = (By.CSS_SELECTOR, "#Activity option")
    routes_distance_input_field = (By.ID, "Distance")
    routes_record_input_field = (By.ID, "RoutePR")
    routes_record_date_input_field = (By.ID, "PRDate")
    routes_desc_input_field = (By.ID, "Notes")


class BikesPageLocators:
    bike_form = (By.ID, "BikeEditForm")
    track_dist_checkbox = (By.ID, "TrackDist")


class ShoesPageLocators:
    shoe_form = (By.ID, "ShoeEditForm")
    shoe_size_dropdown = (By.ID, "ShoeSize")
    shoe_size_dropdown_view = (By.CSS_SELECTOR, "#ShoeSize option")
    shoe_size_dropdown_options = (By.CSS_SELECTOR, "#ShoeSize option")
