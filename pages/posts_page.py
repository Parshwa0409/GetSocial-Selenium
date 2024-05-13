from base.selenium_operations import BaseOperations


class PostsPage(BaseOperations):
    def __init__(self, driver):
        super().__init__(driver=driver)

    def add_post(self, caption):
        self.wait_for_element(self.ID, "post_caption").send_keys(caption)
        self.wait_for_element(self.ID, "post_image").send_keys(
            "/Users/parshwapatil/Desktop/GetSocial/app/assets/images/Bugatti.png")
        self.wait_for_element(self.ID, "create-post-btn").click()

        return self.current_url()

    def like_post(self, post_id: int):
        self.wait_for_element(self.XPATH, f"//button[contains(@class, 'like-btn') and @data-post-id='{post_id}']").click()

