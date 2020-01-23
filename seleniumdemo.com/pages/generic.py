from allure_commons.types import AttachmentType
from selenium.webdriver.common.keys import Keys
from locators import locators
import logging
import allure


class Generic:

    def __init__(self, driver):
        self.driver = driver
        # Generic elements
        self.msg_div = locators.GenericLocators.message_div
        self.error_msg_ul = locators.GenericLocators.error_msg_ul
        self.body_tag = locators.GenericLocators.body_tag
        self.logger = logging.getLogger(__name__)

    @allure.step("Open home page")
    def open_home(self):
        self.logger.info("Open home page")
        self.driver.get("http://seleniumdemo.com/")
        allure.attach(self.driver.get_screenshot_as_png(), name='open_page', attachment_type=AttachmentType.PNG)

    @allure.step("Get message text")
    def get_msg_text(self):
        self.logger.info("Get message text")
        allure.attach(self.driver.get_screenshot_as_png(), name='message', attachment_type=AttachmentType.PNG)
        return self.driver.find_element(*self.msg_div).text

    @allure.step("Get error message text")
    def get_error_msg_text(self):
        self.logger.info("Get error message text")
        self.driver.find_element(*self.body_tag).send_keys(Keys.END)
        allure.attach(self.driver.get_screenshot_as_png(), name='error_message', attachment_type=AttachmentType.PNG)
        return self.driver.find_element(*self.error_msg_ul).text
