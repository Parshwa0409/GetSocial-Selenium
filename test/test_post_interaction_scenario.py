import time

from database.Posts import PostsDB
from pages.home import HomePage
from pages.posts_page import PostsPage
from pages.users_sign_in import UserSignInPage


def test_create_post(launch_browser):
    driver = launch_browser
    sign_in_page = UserSignInPage(driver)
    home_page = HomePage(driver)
    posts_page = PostsPage(driver)
    sign_in_page.login("parshwapatil9@gmail.com")
    home_page.open_tab("Create")
    post_url = posts_page.add_post("Namaste Bugatti")
    global post_id
    post_id = int(post_url.split("/")[-1])
    home_page.logout()

def test_like_post(launch_browser):
    driver = launch_browser
    sign_in_page = UserSignInPage(driver)
    home_page = HomePage(driver)
    posts_page = PostsPage(driver)
    posts_db = PostsDB()
    sign_in_page.login("mani.p@gmail.com")
    time.sleep(2)
    driver.get(f"http://localhost:3000/posts/{post_id}")
    posts_page.like_post(post_id)
    time.sleep(2)
    assert posts_db.get_post_total_likes(post_id) == 1
    home_page.logout()


