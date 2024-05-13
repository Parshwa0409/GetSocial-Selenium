import time

from pages.home import HomePage
from pages.profile import ProfilePage
from pages.stories import StoriesPage
from pages.users_sign_in import UserSignInPage
from database.stories import StoriesDB

import pytest
from selenium import webdriver


@pytest.fixture(scope="module")
def launch_browser():
    global driver
    driver = webdriver.Chrome()
    driver.get('http://localhost:3000/')
    driver.maximize_window()
    driver.implicitly_wait(10)
    yield
    driver.quit()


def test_create_stories(launch_browser):
    sign_in_page = UserSignInPage(driver)
    home_page = HomePage(driver)
    profile_page = ProfilePage(driver)
    sign_in_page.login("parshwapatil9@gmail.com")
    home_page.open_tab("Profile")
    profile_page.add_story()
    home_page.logout()


def test_story_view(launch_browser):
    sign_in_page = UserSignInPage(driver)
    home_page = HomePage(driver)
    stories_page = StoriesPage(driver)
    sign_in_page.login("mani.p@gmail.com")
    home_page.open_tab("Stories")
    story_url = stories_page.view_latest_story()
    home_page.logout()
    # HOW TO DO THIS WITH OUT USING GLOBAL VARIABLES
    global story_id
    story_id = story_url.split("/")[-1]


def test_story_view_increment(launch_browser):
    sign_in_page = UserSignInPage(driver)
    stories_db = StoriesDB()
    sign_in_page.login("parshwapatil9@gmail.com")
    time.sleep(2)
    driver.get(f"http:localhost:3000//stories/{story_id}")
    time.sleep(2)
    assert stories_db.get_story_views(story_id) == 1
