from allure_commons.types import AttachmentType
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from locators.locators import BillingAddressLocators, MyAccountMenuLocators, GenericLocators
import logging
import allure


class BillingAddressPage:

    def __init__(self, driver):
        self.driver = driver
        # Billing Address Page elements
        self.first_name_input = BillingAddressLocators.first_name_input
        self.last_name_input = BillingAddressLocators.last_name_input
        self.addresses_link = MyAccountMenuLocators.addresses_link
        self.edit_link = BillingAddressLocators.edit_billing_address_a
        self.country_select = BillingAddressLocators.country_select
        self.address_input = BillingAddressLocators.address_input
        self.postcode_input = BillingAddressLocators.postcode_input
        self.city_input = BillingAddressLocators.city_input
        self.phone_input = BillingAddressLocators.phone_input
        self.save_address_button = BillingAddressLocators.save_address_button
        self.msg_div = BillingAddressLocators.message_div
        self.allert_address_ul = BillingAddressLocators.allert_address_ul
        self.body_tag = GenericLocators.body_tag
        self.logger = logging.getLogger(__name__)

    @allure.step("Opening addresses page")
    def open_edit_billing_address(self):
        self.logger.info("Opening addresses page")
        self.driver.find_element(*self.addresses_link).click()
        self.driver.find_element(*self.edit_link).click()
        allure.attach(self.driver.get_screenshot_as_png(), name='edit_billing', attachment_type=AttachmentType.PNG)

    @allure.step("Setting personal data: firstname - {1}, lastname - {2}")
    def set_personal_data(self, first_name, last_name):
        self.logger.info("Setting personal data: firstname - {fn} and lastname - {ln}".format(fn=first_name, ln=last_name))
        self.driver.find_element(*self.first_name_input).send_keys(first_name)
        self.driver.find_element(*self.last_name_input).send_keys(last_name)
        allure.attach(self.driver.get_screenshot_as_png(), name='set_personal_data', attachment_type=AttachmentType.PNG)

    @allure.step("Selecting country - {1}")
    def select_country(self, country):
        self.logger.info("Selecting country: {c}".format(c=country))
        select = Select(self.driver.find_element(*self.country_select))
        select.select_by_visible_text(country)
        allure.attach(self.driver.get_screenshot_as_png(), name='select_country', attachment_type=AttachmentType.PNG)

    @allure.step("Setting address: street - {1}, postcode - {2}, city - {3}")
    def set_address(self, street, postcode, city):
        self.logger.info("Setting address: street - {s}, postcode - {p}, city - {c}".format(s=street, p=postcode, c=city))
        self.driver.find_element(*self.address_input).send_keys(street)
        self.driver.find_element(*self.postcode_input).send_keys(postcode)
        self.driver.find_element(*self.city_input).send_keys(city)
        allure.attach(self.driver.get_screenshot_as_png(), name='set_address', attachment_type=AttachmentType.PNG)

    @allure.step("Setting phone number - {1}")
    def set_phone_number(self, number):
        self.logger.info("Setting phone number - {n}".format(n=number))
        self.driver.find_element(*self.phone_input).send_keys(number)
        allure.attach(self.driver.get_screenshot_as_png(), name='set_phone_number', attachment_type=AttachmentType.PNG)

    @allure.step("Saving address")
    def save_address(self):
        self.logger.info("Saving address")
        self.driver.find_element(*self.save_address_button).click()

    @allure.step("Getting message text")
    def get_message_text(self):
        self.logger.info("Getting message text")
        allure.attach(self.driver.get_screenshot_as_png(), name='message', attachment_type=AttachmentType.PNG)
        return self.driver.find_element(*self.msg_div).text

    @allure.step("Getting alert text")
    def get_alert_text(self):
        self.logger.info("Getting alert text")
        self.driver.find_element(*self.body_tag).send_keys(Keys.END)
        allure.attach(self.driver.get_screenshot_as_png(), name='alert', attachment_type=AttachmentType.PNG)
        return self.driver.find_element(*self.allert_address_ul).text
