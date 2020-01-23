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
        self.login_msg_div = locators.MyAccountPageLocators.login_msg_div
        self.lost_password_link = locators.ResetPasswordLocators.lost_password_link
        self.user_login_input = locators.ResetPasswordLocators.user_login_input
        self.reset_password_button = locators.ResetPasswordLocators.reset_password_button
        self.msg_div = locators.GenericLocators.message_div
        self.error_msg_ul = locators.GenericLocators.error_msg_ul
        self.logger = logging.getLogger(__name__)


    @allure.step("Open the login and registration page")
    def open_page(self):
        self.logger.info("Open the login and registration page")
        self.driver.get("http://seleniumdemo.com/?page_id=7")
        allure.attach(self.driver.get_screenshot_as_png(), name='open_page', attachment_type=AttachmentType.PNG)

    @allure.step("Login into the page: user - {1}, password - {2}")
    def log_in(self, username, password):
        self.logger.info("Login into the page by data: user - {u} and password - {p}".format(u=username, p=password))
        self.driver.find_element(*self.username_input).send_keys(username)
        self.driver.find_element(*self.password_input).send_keys(password)
        allure.attach(self.driver.get_screenshot_as_png(), name='login', attachment_type=AttachmentType.PNG)
        self.driver.find_element(*self.password_input).send_keys(Keys.ENTER)

    @allure.step("Create new account: e-mail - {1}, password - {2}")
    def create_account(self, email, password):
        self.logger.info("Create new account by data: e-mail - {e} and password - {p}".format(e=email, p=password))
        self.driver.find_element(*self.reg_email_input).send_keys(email)
        self.driver.find_element(*self.reg_password_input).send_keys(password)
        allure.attach(self.driver.get_screenshot_as_png(), name='new_account', attachment_type=AttachmentType.PNG)
        self.driver.find_element(*self.reg_password_input).send_keys(Keys.ENTER)

    @allure.step("Reset user password - {1}")
    def reset_password(self, email):
        self.logger.info("Reset user password - {u}".format(u=email))
        self.driver.find_element(*self.lost_password_link).click()
        self.driver.find_element(*self.user_login_input).send_keys(email)
        self.driver.find_element(*self.reset_password_button).click()

    @allure.step("Get login message")
    def get_login_msg_text(self):
        self.logger.info("Get login message")
        allure.attach(self.driver.get_screenshot_as_png(), name='logout_link', attachment_type=AttachmentType.PNG)
        return self.driver.find_element(*self.login_msg_div).text
