from pages.billing_address_page import BillingAddressPage
from pages.my_account_page import MyAccountPage
import random
import pytest
import allure


@pytest.mark.usefixtures("setup")
class TestUpdateBillingAddress:

    @allure.title("Updating billing address passed")
    @allure.description("Updating billing address using by correct data")
    def test_update_billing_address_passed(self):
        email = "test{}@mail.com".format(random.randint(0,10000))
        my_account_page = MyAccountPage(self.driver)
        my_account_page.open_page()
        my_account_page.create_account(email, "haslotest12")
        billing_address_page = BillingAddressPage(self.driver)
        billing_address_page.open_edit_billing_address()
        billing_address_page.set_personal_data("John", "Wick")
        billing_address_page.select_country("Poland")
        billing_address_page.set_address("Flower 1", "00-001", "Cracow")
        billing_address_page.set_phone_number("111222333")
        billing_address_page.save_address()

        assert "Address changed successfully." in billing_address_page.get_message_text()

    @allure.title("Updating billing address failed")
    @allure.description("Updating billing address using by incomplete data")
    def test_update_billing_address_failed(self):
        email = "test{}@mail.com".format(random.randint(0,10000))
        my_account_page = MyAccountPage(self.driver)
        my_account_page.open_page()
        my_account_page.create_account(email, "haslotest12")
        billing_address_page = BillingAddressPage(self.driver)
        billing_address_page.open_edit_billing_address()
        billing_address_page.set_personal_data("", "")
        billing_address_page.select_country("Poland")
        billing_address_page.set_address("Flower 1", "00-001", "Cracow")
        billing_address_page.set_phone_number("111222333")
        billing_address_page.save_address()

        assert "First name is a required field." in billing_address_page.get_alert_text()
