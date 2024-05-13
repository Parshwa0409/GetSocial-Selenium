from base.selenium_operations import BaseOperations


class HomePage(BaseOperations):
    def __init__(self, driver):
        super().__init__(driver=driver)

    def open_tab(self, tab_name: str):
        self.wait_for_element(self.XPATH, f"//a[contains(normalize-space(), '{tab_name}')]").click()

    def logout(self):
        self.wait_for_element(self.XPATH, "//button[contains(normalize-space(), 'Settings')]").click()
        self.wait_for_element(self.XPATH, "//button[contains(normalize-space(), 'Logout')]").click()
