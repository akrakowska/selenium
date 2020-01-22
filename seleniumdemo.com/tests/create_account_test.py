from pages.my_account_page import MyAccountPage
import random
import pytest
import allure

@pytest.mark.usefixtures("setup")
class TestCreateAccount:

    @allure.title("Creating account failed")
    @allure.description("Creating account using incorrect data")
    def test_create_account_failed(self):
        my_account_page = MyAccountPage(self.driver)
        my_account_page.open_page()
        my_account_page.create_account("test@mail.com", "haslotest12")

        msg = "An account is already registered with your email address. Please log in."

        assert msg in my_account_page.get_error_msg()

    @allure.title("Creating account passed")
    @allure.description("Creating account using correct data")
    def test_create_account_passed(self):
        email = "test{}@mail.com".format(random.randint(0,10000))
        my_account_page = MyAccountPage(self.driver)
        my_account_page.open_page()
        my_account_page.create_account(email, "haslotest12")

        assert my_account_page.is_logout_link_displayed()
