from base.selenium_operations import SeleniumBaseOperations


class UserSignUpPage(SeleniumBaseOperations):
    def __init__(self, driver):
        super().__init__(driver=driver)

    def register(self, name: str, email: str):

        self.wait_for_element(self.ID, "user_name").send_keys(name)
        self.wait_for_element(self.ID, "user_email").send_keys(email)

        self.wait_for_element(self.ID, "user_password").send_keys("password")
        self.wait_for_element(self.ID, "user_password_confirmation").send_keys("password")
        self.wait_for_element(self.XPATH, "//input[@value='Sign up']").click()

