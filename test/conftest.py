import pytest
from selenium import webdriver


@pytest.fixture(scope="module")
def launch_browser():
    driver = webdriver.Chrome()
    driver.get('http://localhost:3000/')
    driver.maximize_window()
    driver.implicitly_wait(10)
    yield driver
    driver.quit()
