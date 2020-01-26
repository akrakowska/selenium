from pages.shipping_address_page import ShippingAddressPage
from pages.generic import Generic
from pages.my_account_page import MyAccountPage
import random
import pytest
import allure


@pytest.mark.usefixtures("setup")
class TestUpdateShippingAddress:

    @allure.title("TC12: Update shipping address passed")
    @allure.description("Update shipping address with correct data")
    def test_update_shipping_address_passed(self):
        email = "test{}@mail.com".format(random.randint(0,10000))
        my_account_page = MyAccountPage(self.driver)
        my_account_page.open_page()
        my_account_page.create_account(email, "haslotest12")
        shipping_address_page = ShippingAddressPage(self.driver)
        shipping_address_page.open_edit_shipping_address()
        shipping_address_page.set_personal_data("John", "Wick")
        shipping_address_page.select_country("Poland")
        shipping_address_page.set_address("Butterfly 2", "00-002", "Warsaw")
        shipping_address_page.save_address()
        generic = Generic(self.driver)

        assert "Address changed successfully." in generic.get_msg_text()

    @allure.title("TC13: Update shipping address failed")
    @allure.description("Update shipping address with incomplete data")
    def test_update_shipping_address_failed(self):
        email = "test{}@mail.com".format(random.randint(0,10000))
        my_account_page = MyAccountPage(self.driver)
        my_account_page.open_page()
        my_account_page.create_account(email, "haslotest12")
        shipping_address_page = ShippingAddressPage(self.driver)
        shipping_address_page.open_edit_shipping_address()
        shipping_address_page.set_personal_data("", "")
        shipping_address_page.set_address("", "", "")
        shipping_address_page.save_address()
        generic = Generic(self.driver)
        error_msg = generic.get_error_msg_text()

        assert "First name is a required field." in error_msg
        assert "Last name is a required field." in error_msg
        assert "Street address is a required field." in error_msg
        assert "Postcode / ZIP is a required field." in error_msg
        assert "Town / City is a required field." in error_msg
