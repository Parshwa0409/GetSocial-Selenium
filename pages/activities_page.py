from base.selenium_operations import SeleniumBaseOperations


class ActivitiesPage(SeleniumBaseOperations):
    def __init__(self, driver):
        super().__init__(driver=driver)

    def view_latest_shared_post(self, post_user_email):
        self.wait_for_element(self.XPATH, f"//p[contains(text(), 'shared a post by "
                                          f"{post_user_email}')]/following-sibling::a").click()
