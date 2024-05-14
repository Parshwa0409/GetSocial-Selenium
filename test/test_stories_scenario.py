import time
from pages.home_page import HomePage
from pages.profile_page import ProfilePage
from pages.stories_page import StoriesPage
from pages.users_sign_in_page import UserSignInPage
from database.stories import StoriesDB


def test_create_stories(launch_browser):
    driver = launch_browser
    sign_in_page = UserSignInPage(driver)
    home_page = HomePage(driver)
    profile_page = ProfilePage(driver)
    sign_in_page.login("parshwapatil9@gmail.com")
    home_page.open_tab("Profile")
    profile_page.add_story()
    print(driver.current_url)
    home_page.logout()


def test_story_view(launch_browser):
    driver = launch_browser
    sign_in_page = UserSignInPage(driver)
    home_page = HomePage(driver)
    stories_page = StoriesPage(driver)
    sign_in_page.login("mani.p@gmail.com")
    home_page.open_tab("Stories")
    story_url = stories_page.view_latest_story()
    home_page.logout()
    global story_id
    story_id = story_url.split("/")[-1]


def test_story_view_increment(launch_browser):
    driver = launch_browser
    sign_in_page = UserSignInPage(driver)
    stories_db = StoriesDB()
    sign_in_page.login("parshwapatil9@gmail.com")
    time.sleep(2)
    driver.get(f"http://localhost:3000/stories/{story_id}")
    time.sleep(2)
    story_views = stories_db.get_story_views(story_id)
    assert story_views == 1
