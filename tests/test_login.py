from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage


class TestLogin:

    def test_login(self, browser):
        login_page = LoginPage(browser)
        inventory_page = InventoryPage(browser)
        login_page.login()
        assert inventory_page.current_url() == 'https://www.saucedemo.com/inventory.html'
        assert inventory_page.get_products_count() == 6
