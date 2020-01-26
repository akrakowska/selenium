from pages.generic import Generic
from pages.my_account_page import MyAccountPage
import random
import pytest
import allure

@pytest.mark.usefixtures("setup")
class TestCreateAccount:

    @allure.title("TC01: Create account passed")
    @allure.description("Create account using correct data")
    def test_create_account_passed(self):
        email = "test{}@mail.com".format(random.randint(0,10000))
        my_account_page = MyAccountPage(self.driver)
        my_account_page.open_page()
        my_account_page.create_account(email, "haslotest12")

        assert "Hello {}".format(email.split("@")[0]) in my_account_page.get_login_msg_text()

    @allure.title("TC02: Create account failed")
    @allure.description("Create account using incorrect data")
    def test_create_account_failed(self):
        my_account_page = MyAccountPage(self.driver)
        my_account_page.open_page()
        my_account_page.create_account("test@mail.com", "haslotest12")
        generic = Generic(self.driver)

        assert "An account is already registered with your email address. Please log in." in generic.get_error_msg_text()
