from allure_commons.types import AttachmentType
from selenium.webdriver.common.keys import Keys
from locators import locators
import logging
import allure


class SearchProducts:

    def __init__(self, driver):
        self.driver = driver
        # Search Products elements
        self.search_window_link = locators.SearchProductsLocators.search_window_link
        self.search_name_input = locators.SearchProductsLocators.search_name_input
        self.search_results_link = locators.SearchProductsLocators.search_results_link
        self.logger = logging.getLogger(__name__)

    @allure.step("Go to search window")
    def move_search_window(self):
        self.logger.info("Go to search window")
        self.driver.find_element(*self.search_window_link).click()
        allure.attach(self.driver.get_screenshot_as_png(), name='search_window', attachment_type=AttachmentType.PNG)

    @allure.step("Set search data: product name - {1}")
    def set_search_name(self, product_name):
        self.logger.info("Set product name to search: {p}".format(p=product_name))
        self.driver.find_element(*self.search_name_input).send_keys(product_name)
        allure.attach(self.driver.get_screenshot_as_png(), name='search_name', attachment_type=AttachmentType.PNG)
        self.driver.find_element(*self.search_name_input).send_keys(Keys.ENTER)

    @allure.step("Get search results")
    def get_search_results(self):
        search_results = self.driver.find_elements(*self.search_results_link)
        results = [result.get_attribute("textContent") for result in search_results]
        self.logger.info("Available search results are:")
        for result in results:
            self.logger.info(result)
        allure.attach(self.driver.get_screenshot_as_png(), name='search_results', attachment_type=AttachmentType.PNG)
        return results
