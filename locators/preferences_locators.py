from selenium.webdriver.common.by import By


class UserSettingPrefPageLocators:
    user_settings_button = (By.XPATH, "//div[1]/div[3]/div/div[2]/div[1]/div[1]/div/a")
    primary_sport_text = (By.XPATH, "//div[1]/div[3]/div/div[2]/div[1]/div[2]/div/div/p[1]")
    language_text = (By.XPATH, "//div[1]/div[3]/div/div[2]/div[1]/div[2]/div/div/p[2]")
    time_zone_text = (By.XPATH, "//div[1]/div[3]/div/div[2]/div[1]/div[2]/div/div/p[3]")
    primary_sport_dropdown = (By.ID, "PSport")
    primary_sport_dropdown_view = (By.CSS_SELECTOR, "#PSport option")
    primary_sport_dropdown_options = (By.CSS_SELECTOR, "#PSport option")
    spain_language_radio_button = (By.CSS_SELECTOR, "#settings-form .formSep .radio:nth-child(4) input")
    english_language_radio_button = (By.CSS_SELECTOR, "#settings-form .formSep .radio:nth-child(2) input")
    time_zone_dropdown = (By.ID, "TZone")
    time_zone_dropdown_view = (By.CSS_SELECTOR, "#TZone option")
    time_zone_dropdown_options = (By.CSS_SELECTOR, "#TZone option")
    save_changes_button = (By.ID, "saveButtonSettings")


class UserProfilePrefPageLocators:
    edit_profile_button = (By.XPATH, "//div[1]/div[3]/div/div[1]/div[1]/div[1]/div/a")
    name_text = (By.XPATH, "//div[1]/div[3]/div/div[1]/div[1]/div[2]/div/div/p[1]")
    email_text = (By.XPATH, "//div[1]/div[3]/div/div[1]/div[1]/div[2]/div/div/p[2]")
    birthday_text = (By.XPATH, "//div[1]/div[3]/div/div[1]/div[1]/div[2]/div/div/p[4]")
    city_text = (By.XPATH, "//div[1]/div[3]/div/div[1]/div[1]/div[2]/div/div/p[8]")
    zip_code_text = (By.XPATH, "//div[1]/div[3]/div/div[1]/div[1]/div[2]/div/div/p[9]")
    first_name_input_field = (By.ID, "fname")
    last_name_input_field = (By.ID, "lname")
    email_changed_link = (By.CSS_SELECTOR, ".help-block a")
    email_input_field = (By.ID, "email")
    password_input_field = (By.ID, "upassword")
    save_change_email_btn = (By.ID, "saveButton")
    male_radio_button = (By.ID, "male")
    birthday_input_field = (By.ID, "BDay")
    country_dropdown = (By.ID, "Country")
    country_dropdown_view = (By.CSS_SELECTOR, "#Country option")
    country_dropdown_options = (By.CSS_SELECTOR, "#Country option")
    city_input_field = (By.ID, "City")
    zip_code_input_field = (By.ID, "Zip")
    delete_my_account_link = (By.ID, "del-user")
    ok_btn = (By.XPATH, "//div[@class='modal-footer']/a[contains(.,'OK')]")
    submit_button = (By.ID, "saveButtonProfile")


class SocialMediaPrefPageLocators:
    edit_social_media_button = (By.XPATH, "//div[1]/div[3]/div/div[1]/div[3]/div[1]/div/a")
    twitter_button = (By.CSS_SELECTOR, "#form-social a")


class SecuritySettingPrefPageLocators:
    edit_security_settings = (By.XPATH, "//div[1]/div[3]/div/div[2]/div[2]/div[1]/div/a")
    current_pass_input_field = (By.ID, "CurrentPassword")
    new_pass_input_field = (By.ID, "password_meter")
    re_new_pass_input_field = (By.ID, "RePassword")
    submit_change_pass_btn = (By.ID, "saveButtonPass")
    security_question_input_field = (By.ID, "SecQuestion")
    security_answer_input_field = (By.ID, "SecAnswer")
    enter_current_pass_input_field = (By.ID, "VerifyPass")
    update_security_question_btn = (By.ID, "saveButtonQuestion")


class CalendarSyncPrefPageLocators:
    edit_sync_button = (By.XPATH, "//div[1]/div[3]/div/div[1]/div[2]/div[1]/div/a")
    turn_off_radio_button = (By.ID, "SyncOff")
    turn_on_radio_button = (By.ID, "SyncOn")
    save_changes_button1 = (By.ID, "saveButtonSync")
    calendar_sync_status_text = (By.XPATH, "//div[1]/div[3]/div/div[1]/div[2]/div[2]/div/div/p[1]/span")
