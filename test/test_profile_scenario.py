import time

from pages.home_page import HomePage
from pages.search_page import SearchPage
from pages.users_sign_in_page import UserSignInPage
from pages.users_sign_up_page import UserSignUpPage


def test_profile_actions(launch_browser):
    driver = launch_browser
    user_sign_in_page = UserSignInPage(driver)
    user_sign_up_page = UserSignUpPage(driver)
    home_page = HomePage(driver)
    search_page = SearchPage(driver)

    user_sign_in_page.open_sig_up_form()
    user_sign_up_page.register("Test User", "test_user@gmail.com", "password")
    home_page.open_tab("Search")
    search_page.search_by_name("Parshwa")
    time.sleep(10)




