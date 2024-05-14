from base.selenium_operations import SeleniumBaseOperations


class PostsPage(SeleniumBaseOperations):
    def __init__(self, driver):
        super().__init__(driver=driver)

    def add_post(self, caption):
        self.wait_for_element(self.ID, "post_caption").send_keys(caption)
        self.wait_for_element(self.ID, "post_image").send_keys(
            "/Users/pbpatil/Desktop/GetSocial/app/assets/images/Bugatti.png")
        self.wait_for_element(self.ID, "create-post-btn").click()

        return self.current_url()

    def like_post(self, post_id: int):
        self.wait_for_element(self.XPATH,
                              f"//button[contains(@class, 'like-btn') and @data-post-id='{post_id}']").click()

    def comment_on_post(self, post_id: int, comment: str):
        self.wait_for_element(self.XPATH,
                              f"//button[contains(@class, 'comment-btn') and @data-post-id='{post_id}']").click()
        self.wait_for_element(self.XPATH, "//input[@placeholder = 'Type your comment here']").send_keys(comment)
        self.wait_for_element(self.XPATH, "//button[contains(normalize-space(), 'Post Comment')]").click()
        self.wait_for_element(self.ID, "comments-modal-close").click()

    def share_post(self, post_id: int):
        self.wait_for_element(self.XPATH,
                              f"//button[contains(@class, 'share-btn') and @data-post-id='{post_id}']").click()
        share_btn = self.wait_for_element(self.XPATH, "//button[contains(@class, 'share-post-btn')]")
        share_btn.click()
        self.wait_for_element(self.ID, "share-post-modal-close").click()
        return share_btn.get_attribute("data-user-id")
