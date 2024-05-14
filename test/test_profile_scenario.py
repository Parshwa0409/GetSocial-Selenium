from pages.users_sign_in_page import UserSignInPage
from pages.users_sign_up_page import UserSignUpPage


def test_sign_up(launch_browser):
    driver = launch_browser
    user_sign_in_page = UserSignInPage(driver)
    user_sign_up_page = UserSignUpPage(driver)

    user_sign_in_page.open_sig_up_form()
    user_sign_up_page.register("Test User", "test_user@gmail.com", "password")


