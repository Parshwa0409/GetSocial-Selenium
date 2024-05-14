from base.selenium_operations import SeleniumBaseOperations


class SearchPage(SeleniumBaseOperations):
    def __init__(self, driver):
        super().__init__(driver=driver)

    def search_by_name(self, name):
        self.wait_for_element(self.ID, "name").send_keys(name)
        self.wait_for_element(self.ID, "query-btn").click()
