from base.selenium_operations import SeleniumBaseOperations


class ActivitiesPage(SeleniumBaseOperations):
    def __init__(self, driver):
        super().__init__(driver=driver)

    def view_latest_shared_post(self, post_user_email):
        self.wait_for_element(self.XPATH, f"//p[contains(text(), 'shared a post by "
                                          f"{post_user_email}')]/following-sibling::a").click()

    def __view_requests(self, request_type):
        self.wait_for_element(self.XPATH, f"//h3[contains(text(), '{request_type}')]//following-sibling::a").click()

    def view_follow_request(self):
        self.__view_requests("Follow")

    def view_pending_request(self):
        self.__view_requests("Pending")

    def accept_latest_follow_request(self, email):
        self.wait_for_element(self.XPATH,
                              f"//h4[contains(text(), '{email}')]//ancestor::div[contains(@class, "
                              f"'user-details')]/following-sibling::div/button[1]").click()
