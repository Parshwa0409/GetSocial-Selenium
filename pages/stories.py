import time

from base.selenium_operations import BaseOperations


class StoriesPage(BaseOperations):
    def __init__(self, driver):
        super().__init__(driver=driver)

    def view_latest_story(self):
        self.wait_for_element(self.XPATH, "//a[contains(normalize-space(), 'View Story')]").click()
        time.sleep(1)
        return self.current_url()
