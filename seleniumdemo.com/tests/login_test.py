from pages.generic import Generic
from pages.my_account_page import MyAccountPage
import pytest
import allure


@pytest.mark.usefixtures("setup")
class TestLogIn:

    @allure.title("TC03: Login passed")
    @allure.description("Login using correct data")
    def test_log_in_passed(self):
        my_account_page = MyAccountPage(self.driver)
        my_account_page.open_page()
        my_account_page.log_in("test@mail.com", "haslotest12")

        assert "Hello test" in my_account_page.get_login_msg_text()

    @allure.title("TC04: Login failed")
    @allure.description("Login using incorrect data")
    def test_log_in_failed(self):
        my_account_page = MyAccountPage(self.driver)
        my_account_page.open_page()
        my_account_page.log_in("test@mail.com", "invalidpassword")
        generic = Generic(self.driver)

        assert "ERROR: Incorrect username or password." in generic.get_error_msg_text()
