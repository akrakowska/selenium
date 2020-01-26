from pages.generic import Generic
import pytest
import allure
from pages.navigation_menu import NavigationMenu


@pytest.mark.usefixtures("setup")
class TestNavigationMenu:

    @allure.title("Navigation menu - Cart")
    @allure.description("Move to subpage Cart using Navigaton Menu")
    def test_move_cart(self):
        open_home = Generic(self.driver)
        open_home.open_home()
        nav_menu = NavigationMenu(self.driver)
        nav_menu.move_cart()

        assert "Cart" in nav_menu.get_page_title()

    @allure.title("Navigation menu - Shop")
    @allure.description("Move to subpage Shop using Navigaton Menu")
    def test_move_shop(self):
        open_home = Generic(self.driver)
        open_home.open_home()
        nav_menu = NavigationMenu(self.driver)
        nav_menu.move_shop()

        assert "Shop" in nav_menu.get_page_title()

    @allure.title("Navigation menu - My account")
    @allure.description("Move to subpage My account using Navigaton Menu")
    def test_move_my_account(self):
        open_home = Generic(self.driver)
        open_home.open_home()
        nav_menu = NavigationMenu(self.driver)
        nav_menu.move_my_account()

        assert "My account" in nav_menu.get_page_title()
