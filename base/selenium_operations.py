import time

from selenium.common import TimeoutException, NoSuchElementException
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BaseOperations:
    def __init__(self, driver):
        self.driver = driver
        self.ID = "id"
        self.XPATH = "xpath"
        self.LINK_TEXT = "link text"
        self.PARTIAL_LINK_TEXT = "partial link text"
        self.NAME = "name"
        self.TAG_NAME = "tag name"
        self.CLASS_NAME = "class name"
        self.CSS_SELECTOR = "css selector"

    def current_url(self):
        return self.driver.current_url

    def implicit_wait(self, sec=7):
        self.driver.implicitly_wait(sec)

    def wait_for_element(self,
                         locator_tag,
                         locator,
                         multiple=False) -> WebElement or TimeoutException or NoSuchElementException:

        time.sleep(1.5)

        if not multiple:
            return WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((locator_tag, locator))
            )
        else:
            return WebDriverWait(self.driver, 10).until(
                EC.presence_of_all_elements_located((locator_tag, locator))
            )

    def get_element_classes(self, element):
        element_class = element.get_attribute("class")
        return element_class