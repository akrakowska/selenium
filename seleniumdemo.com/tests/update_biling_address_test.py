from pages.billing_address_page import BillingAddressPage
from pages.generic import Generic
from pages.my_account_page import MyAccountPage
import random
import pytest
import allure


@pytest.mark.usefixtures("setup")
class TestUpdateBillingAddress:

    @allure.title("Update billing address passed")
    @allure.description("Update billing address with correct data")
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
        billing_address_page.set_email_address(email)
        billing_address_page.save_address()
        generic = Generic(self.driver)

        assert "Address changed successfully." in generic.get_msg_text()

    @allure.title("Update billing address failed")
    @allure.description("Update billing address with incomplete data")
    def test_update_billing_address_failed(self):
        email = "test{}@mail.com".format(random.randint(0,10000))
        my_account_page = MyAccountPage(self.driver)
        my_account_page.open_page()
        my_account_page.create_account(email, "haslotest12")
        billing_address_page = BillingAddressPage(self.driver)
        billing_address_page.open_edit_billing_address()
        billing_address_page.set_personal_data("", "")
        billing_address_page.set_address("", "", "")
        billing_address_page.set_phone_number("")
        billing_address_page.set_email_address("")
        billing_address_page.save_address()
        generic = Generic(self.driver)

        assert "First name is a required field." in generic.get_error_msg_text()
        assert "Last name is a required field." in generic.get_error_msg_text()
        assert "Street address is a required field." in generic.get_error_msg_text()
        assert "Postcode / ZIP is a required field." in generic.get_error_msg_text()
        assert "Town / City is a required field." in generic.get_error_msg_text()
        assert "Phone is a required field." in generic.get_error_msg_text()
        assert "Email address is a required field." in generic.get_error_msg_text()
