from allure_commons.types import AttachmentType
from locators import locators
import logging
import allure


class NavigationMenu:

    def __init__(self, driver):
        self.driver = driver
        # Navigation menu elements
        self.cart_span = locators.NavigationMenuLocators.cart_span
        self.shop_span = locators.NavigationMenuLocators.shop_span
        self.my_account_span = locators.NavigationMenuLocators.my_account_span
        self.page_title_span = locators.NavigationMenuLocators.page_title_span
        self.logger = logging.getLogger(__name__)

    @allure.step("Move to subpage Cart using Navigation Menu")
    def move_cart(self):
        self.logger.info("Move to subpage Cart using Navigation Menu")
        self.driver.find_element(*self.cart_span).click()
        allure.attach(self.driver.get_screenshot_as_png(), name='cart', attachment_type=AttachmentType.PNG)

    @allure.step("Move to subpage Shop using Navigation Menu")
    def move_shop(self):
        self.logger.info("Move to subpage Shop using Navigation Menu")
        self.driver.find_element(*self.shop_span).click()
        allure.attach(self.driver.get_screenshot_as_png(), name='shop', attachment_type=AttachmentType.PNG)

    @allure.step("Move to subpage My account using Navigation Menu")
    def move_my_account(self):
        self.logger.info("Move to subpage My account using Navigation Menu")
        self.driver.find_element(*self.my_account_span).click()
        allure.attach(self.driver.get_screenshot_as_png(), name='my_account', attachment_type=AttachmentType.PNG)

    @allure.step("Get page title")
    def get_page_title(self):
        self.logger.info("Get page title")
        allure.attach(self.driver.get_screenshot_as_png(), name='page_title', attachment_type=AttachmentType.PNG)
        return self.driver.find_element(*self.page_title_span).text
