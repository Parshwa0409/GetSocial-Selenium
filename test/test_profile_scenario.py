import time

from faker import Faker

from database.users import UsersDB
from pages.activities_page import ActivitiesPage
from pages.home_page import HomePage
from pages.profile_page import ProfilePage
from pages.search_page import SearchPage
from pages.users_sign_in_page import UserSignInPage
from pages.users_sign_up_page import UserSignUpPage


def test_profile_actions(launch_browser):
    driver = launch_browser

    QUERY_NAME = "Test User"
    QUERY_EMAIL = "parshwapatil9@gmail.com"
    faker = Faker()
    sign_up_email = faker.email()

    user_sign_in_page = UserSignInPage(driver)
    user_sign_up_page = UserSignUpPage(driver)
    home_page = HomePage(driver)
    profile_page = ProfilePage(driver)
    search_page = SearchPage(driver)
    activities_page = ActivitiesPage(driver)

    users_table = UsersDB()

    user_sign_in_page.open_sign_up_form()
    user_sign_up_page.register(QUERY_NAME, sign_up_email)
    home_page.open_tab("Search")
    search_page.search_by_name(QUERY_NAME)
    result_row_count = search_page.get_result_count()
    queried_users_count = users_table.find_count_of_users_with_like_name(QUERY_NAME)
    assert result_row_count == queried_users_count
    search_page.clear_name_input()

    search_page.search_by_email(QUERY_EMAIL)
    result_row_count = search_page.get_result_count()
    queried_users_count = users_table.find_count_of_users_with_email(QUERY_EMAIL)
    assert result_row_count == queried_users_count
    search_page.clear_email_input()
    search_page.view_profile(QUERY_EMAIL)
    profile_page.send_follow_request()
    home_page.logout()

    user_sign_in_page.login(QUERY_EMAIL)
    home_page.open_tab("Activity")
    activities_page.view_follow_request()
    activities_page.accept_latest_follow_request(sign_up_email)
    time.sleep(3)
