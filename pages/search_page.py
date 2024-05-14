from base.selenium_operations import SeleniumBaseOperations


class SearchPage(SeleniumBaseOperations):
    def __init__(self, driver):
        super().__init__(driver=driver)

    def search_by_name(self, name):
        self.wait_for_element(self.ID, "name").send_keys(name)
        self.wait_for_element(self.ID, "query-btn").click()

    def search_by_email(self, email):
        self.wait_for_element(self.ID, "email").send_keys(email)
        self.wait_for_element(self.ID, "query-btn").click()

    def get_result_count(self):
        return len(self.wait_for_element(self.CLASS_NAME, "result-row", multiple=True))


    def __clear_input(self, locator_tag: str, locator: str):
        self.wait_for_element(locator_tag, locator).clear()

    def clear_name_input(self):
        self.__clear_input(self.ID, "name")

    def clear_email_input(self):
        self.__clear_input(self.ID, "email")