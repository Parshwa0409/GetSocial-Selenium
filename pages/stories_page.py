import time

from base.selenium_operations import SeleniumBaseOperations


class StoriesPage(SeleniumBaseOperations):
    def __init__(self, driver):
        super().__init__(driver=driver)

    def view_latest_story(self, text, story_id):
        self.wait_for_element(self.XPATH,
                              f"//a[contains(normalize-space(), '{text}') and @data-story-id='{story_id}']").click()
        time.sleep(1)
