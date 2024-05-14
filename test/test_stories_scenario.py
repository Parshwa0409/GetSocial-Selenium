import time
from pages.home_page import HomePage
from pages.profile_page import ProfilePage
from pages.stories_page import StoriesPage
from pages.users_sign_in_page import UserSignInPage
from database.stories import StoriesDB


def test_story_scenerios(launch_browser):
    driver = launch_browser
    sign_in_page = UserSignInPage(driver)
    home_page = HomePage(driver)
    profile_page = ProfilePage(driver)
    stories_page = StoriesPage(driver)

    stories_db = StoriesDB()

    sign_in_page.login("parshwapatil9@gmail.com")
    home_page.open_tab("Profile")
    profile_page.add_story()
    # time.sleep(2)
    STORY_ID = stories_page.current_url().split("/")[-1]
    story_views_count_v1 = stories_db.x(STORY_ID)
    home_page.logout()

    sign_in_page.login("mani.p@gmail.com")
    home_page.open_tab("Stories")
    stories_page.view_latest_story("View Story", STORY_ID)
    # time.sleep(2)
    story_views_count_v2 = stories_db.get_story_views(STORY_ID)
    assert story_views_count_v2 == (story_views_count_v1 + 1)

    home_page.open_tab("Stories")
    stories_page.view_latest_story("View Again", STORY_ID)
    # time.sleep(2)
    story_views_count_v3 = stories_db.get_story_views(STORY_ID)
    assert story_views_count_v3 == story_views_count_v2
    home_page.logout()

    sign_in_page.login("parshwapatil9@gmail.com")
    time.sleep(2)
    driver.get(f"http://localhost:3000/stories/{STORY_ID}")

