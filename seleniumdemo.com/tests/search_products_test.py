from pages.search_products import SearchProducts
from pages.generic import Generic
import pytest
import allure


@pytest.mark.usefixtures("setup")
class TestSearchProducts:

    @allure.title("TC14: Search products passed")
    @allure.description("Search using correct product name")
    def test_search_products_passed(self):
        open_home = Generic(self.driver)
        open_home.open_home()
        search_products = SearchProducts(self.driver)
        search_products.move_search_window()
        search_products.set_search_name("selenium")
        results = search_products.get_search_results()

        for result in results:
            assert "selenium" in result.lower()

    @allure.title("TC15: Search products failed")
    @allure.description("Search using incorrect product name")
    def test_search_products_failed(self):
        open_home = Generic(self.driver)
        open_home.open_home()
        search_products = SearchProducts(self.driver)
        search_products.move_search_window()
        search_products.set_search_name("non-existing product")
        results = search_products.get_search_results()

        assert "Nothing Found" in results
