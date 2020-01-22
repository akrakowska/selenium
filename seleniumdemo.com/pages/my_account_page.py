from allure_commons.types import AttachmentType
from selenium.webdriver.common.keys import Keys
from locators import locators
import logging
import allure


class MyAccountPage:

    def __init__(self, driver):
        self.driver = driver
        # My Account Page elements
        self.username_input = locators.MyAccountPageLocators.username_input
        self.password_input = locators.MyAccountPageLocators.password_input
        self.reg_email_input = locators.MyAccountPageLocators.reg_email_input
        self.reg_password_input = locators.MyAccountPageLocators.reg_password_input
        self.logout_link = locators.MyAccountPageLocators.logout_link
        self.error_msg = locators.MyAccountPageLocators.error_msg
        self.logger = logging.getLogger(__name__)

    @allure.step("Opening the login and registration page")
    def open_page(self):
        self.logger.info("Opening the login and registration page")
        self.driver.get("http://seleniumdemo.com/?page_id=7")
        allure.attach(self.driver.get_screenshot_as_png(), name='open_page', attachment_type=AttachmentType.PNG)

    @allure.step("Login into the page: user - {1}, password - {2}")
    def log_in(self, username, password):
        self.logger.info("Login into the page by data: user - {u} and password - {p}".format(u=username, p=password))
        self.driver.find_element(*self.username_input).send_keys(username)
        self.driver.find_element(*self.password_input).send_keys(password)
        allure.attach(self.driver.get_screenshot_as_png(), name='login', attachment_type=AttachmentType.PNG)
        self.driver.find_element(*self.password_input).send_keys(Keys.ENTER)

    @allure.step("Creating new account: e-mail - {1}, password - {2}")
    def create_account(self, email, password):
        self.logger.info("Creating new account by data: e-mail - {e} and password - {p}".format(e=email, p=password))
        self.driver.find_element(*self.reg_email_input).send_keys(email)
        self.driver.find_element(*self.reg_password_input).send_keys(password)
        allure.attach(self.driver.get_screenshot_as_png(), name='new_account', attachment_type=AttachmentType.PNG)
        self.driver.find_element(*self.reg_password_input).send_keys(Keys.ENTER)

    @allure.step("Checking logout link displayed")
    def is_logout_link_displayed(self):
        self.logger.info("Checking logout link displayed")
        allure.attach(self.driver.get_screenshot_as_png(), name='logout_link', attachment_type=AttachmentType.PNG)
        return self.driver.find_element(*self.logout_link).is_displayed()

    @allure.step("Getting error message")
    def get_error_msg(self):
        self.logger.info("Getting error message")
        allure.attach(self.driver.get_screenshot_as_png(), name='error_message', attachment_type=AttachmentType.PNG)
        return self.driver.find_element(*self.error_msg).text
