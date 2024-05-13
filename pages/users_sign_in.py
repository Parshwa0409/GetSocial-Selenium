from base.selenium_operations import BaseOperations


class UserSignInPage(BaseOperations):
    def __init__(self, driver):
        super().__init__(driver=driver)

    def login(self, email):
        self.wait_for_element(self.ID, "user_email").send_keys(email)
        self.wait_for_element(self.ID, "user_password").send_keys("password")
        self.wait_for_element(self.XPATH, "//input[@value='Log in']").click()

