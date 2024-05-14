import time

from base.selenium_operations import SeleniumBaseOperations
from faker import Faker


class UserSignUpPage(SeleniumBaseOperations):
    def __init__(self, driver):
        super().__init__(driver=driver)

    def register(self, name):
        faker = Faker()
        self.wait_for_element(self.ID, "user_name").send_keys(name)
        self.wait_for_element(self.ID, "user_email").send_keys(faker.email())

        self.wait_for_element(self.ID, "user_password").send_keys("password")
        self.wait_for_element(self.ID, "user_password_confirmation").send_keys("password")
        self.wait_for_element(self.XPATH, "//input[@value='Sign up']").click()

