from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.product_page import ProductPage
from pages.cart_page import CartPage


class TestProduct:

    def test_open_product(self, browser):
        login_page = LoginPage(browser)
        inventory_page = InventoryPage(browser)
        product_page = ProductPage(browser)
        login_page.login()
        inventory_page.open_product()
        assert product_page.current_url() == 'https://www.saucedemo.com/inventory-item.html?id=4'
        assert product_page.is_product_icon_displayed() == 1
        assert product_page.is_product_title_displayed() == 1
        assert product_page.is_product_price_displayed() == 1
        assert product_page.is_product_description_displayed() == 1

    def test_product_title(self, browser):
        login_page = LoginPage(browser)
        inventory_page = InventoryPage(browser)
        product_page = ProductPage(browser)
        login_page.login()
        product_title_on_inventory_page = inventory_page.get_products_names()
        inventory_page.open_product()
        product_title_on_product_page = product_page.get_product_name()
        assert product_title_on_inventory_page[0] == product_title_on_product_page

    def test_product_price(self, browser):
        login_page = LoginPage(browser)
        inventory_page = InventoryPage(browser)
        product_page = ProductPage(browser)
        login_page.login()
        product_price_on_inventory_page = inventory_page.get_products_prices()
        inventory_page.open_product()
        product_price_on_product_page = product_page.get_product_price()
        assert product_price_on_inventory_page[0] == product_price_on_product_page

    def test_add_product_to_cart(self, browser):
        login_page = LoginPage(browser)
        inventory_page = InventoryPage(browser)
        product_page = ProductPage(browser)
        login_page.login()
        inventory_page.open_product()
        product_page.add_product_to_cart()
        assert inventory_page.get_count_of_added_products() == '1'
        assert product_page.is_remove_button_present() == 1

    def test_added_product_in_cart(self, browser):
        login_page = LoginPage(browser)
        inventory_page = InventoryPage(browser)
        product_page = ProductPage(browser)
        cart_page = CartPage(browser)
        login_page.login()
        inventory_page.open_product()
        product_name = product_page.get_product_name()
        product_page.add_product_to_cart()
        inventory_page.open_cart()
        assert cart_page.get_added_product_name() == product_name

    def test_remove_product(self, browser):
        login_page = LoginPage(browser)
        inventory_page = InventoryPage(browser)
        product_page = ProductPage(browser)
        login_page.login()
        inventory_page.open_product()
        product_page.add_product_to_cart()
        product_page.remove_product()
        assert product_page.is_remove_button_present() == 0
        assert inventory_page.is_shopping_cart_counter_displayed() == 0

    def test_back_to_products(self, browser):
        login_page = LoginPage(browser)
        inventory_page = InventoryPage(browser)
        product_page = ProductPage(browser)
        login_page.login()
        inventory_page.open_product()
        product_page.back_to_products()
        assert inventory_page.current_url() == 'https://www.saucedemo.com/inventory.html'
        assert inventory_page.get_products_count() == 6
