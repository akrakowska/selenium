from pages.generic import Generic
from pages.my_account_page import MyAccountPage
import pytest
import allure

@pytest.mark.usefixtures("setup")
class TestResetPassword:

    @allure.title("TC05: Reset password passed")
    @allure.description("Reset password using correct data")
    def test_reset_password_passed(self):
        my_account_page = MyAccountPage(self.driver)
        my_account_page.open_page()
        my_account_page.reset_password("test@mail.com")
        generic = Generic(self.driver)

        assert "Password reset email has been sent." in generic.get_msg_text()

    @allure.title("TC06: Reset password failed")
    @allure.description("Reset password using incorrect data")
    def test_reset_password_failed(self):
        my_account_page = MyAccountPage(self.driver)
        my_account_page.open_page()
        my_account_page.reset_password("non_existent_email@mail.com")
        generic = Generic(self.driver)

        assert "Invalid username or email." in generic.get_error_msg_text()
