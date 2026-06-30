import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select, WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class StudentFormPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

        self.title = (By.XPATH, ".//div/h1")
        self.element_block = (By.CLASS_NAME, "accordion-button")
        self.name = (By.ID, "name")
        self.email = (By.ID, "email")
        self.gender = (By.ID, "gender")
        self.mobile = (By.ID, "mobile")
        self.dob = (By.ID, "dob")
        self.subjects = (By.ID, "subjects")
        self.picture = (By.ID, "picture")
        self.state = (By.ID, "state")
        self.city = (By.ID, "city")
        self.submit_btn = (By.XPATH, "//input[@type='submit']")

    def get_title_text(self):
        return self.wait.until(EC.visibility_of_element_located(self.title)).text

    def click_element_block(self):
        self.wait.until(EC.element_to_be_clickable(self.element_block)).click()

    def enter_name(self, value):
        element = self.wait.until(EC.visibility_of_element_located(self.name))
        element.clear()
        element.send_keys(value)

    def enter_email(self, value):
        email_name = self.wait.until(EC.visibility_of_element_located(self.email))
        email_name.clear()
        email_name.send_keys(value)

    def select_gender(self):
        self.wait.until(EC.element_to_be_clickable(self.gender)).click()

    def enter_mobile(self, value):
        mob = self.wait.until(EC.visibility_of_element_located(self.mobile))
        mob.clear()
        mob.send_keys(value)

    def date_of_birth(self, value):
        date = self.wait.until(EC.visibility_of_element_located(self.dob))
        date.clear()
        date.send_keys(value)

    def enter_subjects(self, value):
        subs = self.wait.until(EC.visibility_of_element_located(self.subjects))
        subs.clear()
        subs.send_keys(value)

    def upload_file(self, file_path):
        upload_file = self.wait.until(EC.presence_of_element_located(self.picture))
        upload_file.send_keys(file_path)

    def select_state(self, value):
        state_dropdown = self.wait.until(EC.presence_of_element_located(self.state))
        Select(state_dropdown).select_by_visible_text(value)

    def select_city(self, value):
        city_dropdown = self.wait.until(EC.presence_of_element_located(self.city))
        Select(city_dropdown).select_by_visible_text(value)

    def click_submit(self):
        element = self.wait.until(EC.presence_of_element_located(self.submit_btn))
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)
        time.sleep(1)
        self.wait.until(EC.element_to_be_clickable(self.submit_btn))
        element.click()