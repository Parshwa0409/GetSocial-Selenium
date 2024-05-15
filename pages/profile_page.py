from base.selenium_operations import SeleniumBaseOperations


class ProfilePage(SeleniumBaseOperations):
    def __init__(self, driver):
        super().__init__(driver=driver)

    def add_story(self):
        self.wait_for_element(self.XPATH, "//button[contains(normalize-space(), 'Add Story')]").click()
        self.wait_for_element(self.ID, "story-pic").send_keys(
            "/Users/pbpatil/Desktop/GetSocial/app/assets/images/Bugatti.png")
        self.wait_for_element(self.ID, "create-story-btn").click()

    def send_follow_request(self):
        self.wait_for_element(self.XPATH, "//button[contains(text(), 'Follow')]").click()

    def open_edit_profile(self):
        self.wait_for_element(self.XPATH, "//button[contains(text(), 'Edit Profile')]").click()

    def edit_profile(self):
        self.wait_for_element(self.ID, "user_name").clear()
        self.wait_for_element(self.ID, "user_name").send_keys("Test User Updated Name")
        self.wait_for_element(self.XPATH, "//input[contains(@value, 'Update My Info')]").click()



