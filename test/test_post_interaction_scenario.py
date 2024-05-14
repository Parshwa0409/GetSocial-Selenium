import time

from database.posts import PostsDB
from database.users import UsersDB
from pages.activities_page import ActivitiesPage
from pages.home_page import HomePage
from pages.posts_page import PostsPage
from pages.users_sign_in_page import UserSignInPage


def get_id(url: str):
    return int(url.split("/")[-1])


def test_new_post_interaction(launch_browser):
    driver = launch_browser

    # pages
    sign_in_page = UserSignInPage(driver)
    home_page = HomePage(driver)
    posts_page = PostsPage(driver)
    activities_page = ActivitiesPage(driver)

    # database
    posts_table = PostsDB()
    users_table = UsersDB()

    # automation
    sign_in_page.login("parshwapatil9@gmail.com")
    home_page.open_tab("Create")
    pan_count = home_page.get_post_activity_notifications_count()
    post_url = posts_page.add_post("Namaste Bugatti")
    POST_ID = get_id(post_url)
    home_page.logout()

    sign_in_page.login("lisha2002@gmail.com")
    home_page.get_url(f"http://localhost:3000/posts/{POST_ID}")

    posts_page.like_post(POST_ID)
    time.sleep(2)
    total_likes = posts_table.get_post_total_likes(POST_ID)
    assert total_likes == 1

    posts_page.comment_on_post(POST_ID, f"New Comment on Post-{POST_ID}")
    time.sleep(2)
    total_comments = posts_table.get_post_total_comments(POST_ID)
    assert total_comments == 1

    user_id = posts_page.share_post(POST_ID)
    home_page.logout()
    user_email = users_table.find_user_email_by_id(user_id)
    sign_in_page.login(user_email)
    home_page.open_tab("Activity")
    activities_page.view_latest_shared_post(post_user_email=user_email)
    time.sleep(2)
    assert home_page.get_post_activity_notifications_count() == (pan_count + 3)
