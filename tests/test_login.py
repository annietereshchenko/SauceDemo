from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage


class TestLogin:

    def test_login(self, browser):
        login_page = LoginPage(browser)
        inventory_page = InventoryPage(browser)
        login_page.enter_name('standard_user')
        login_page.enter_password('secret_sauce')
        login_page.click_on_login()
        assert inventory_page.current_url() == 'https://www.saucedemo.com/inventory.html'
