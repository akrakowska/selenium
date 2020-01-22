from pages.my_account_page import MyAccountPage
import pytest
import allure


@pytest.mark.usefixtures("setup")
class TestLogIn:

    @allure.title("Login passed")
    @allure.description("Login using correct data")
    def test_log_in_passed(self):
        my_account_page = MyAccountPage(self.driver)
        my_account_page.open_page()
        my_account_page.log_in("test@mail.com", "haslotest12")

        assert my_account_page.is_logout_link_displayed()

    @allure.title("Login failed")
    @allure.description("Login using incorrect data")
    def test_log_in_failed(self):
        my_account_page = MyAccountPage(self.driver)
        my_account_page.open_page()
        my_account_page.log_in("test@mail.com", "invalidpassword")

        assert "ERROR: Incorrect username or password." in my_account_page.get_error_msg()
