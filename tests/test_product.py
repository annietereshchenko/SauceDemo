from pages.inventory_page import InventoryPage
from pages.product_page import ProductPage
from pages.cart_page import CartPage
from pages.common_logic import CommonLogic


class TestProduct:

    def test_open_product(self, browser):
        inventory_page = InventoryPage(browser)
        product_page = ProductPage(browser)
        common_logic = CommonLogic(browser)
        common_logic.login()
        inventory_page.open_product()
        assert product_page.current_url() == 'https://www.saucedemo.com/inventory-item.html?id=4'

    def test_display_product_icon(self, browser):
        inventory_page = InventoryPage(browser)
        product_page = ProductPage(browser)
        common_logic = CommonLogic(browser)
        common_logic.login()
        inventory_page.open_product()
        assert product_page.is_product_icon_displayed() == 1

    def test_display_product_title(self, browser):
        inventory_page = InventoryPage(browser)
        product_page = ProductPage(browser)
        common_logic = CommonLogic(browser)
        common_logic.login()
        inventory_page.open_product()
        assert product_page.is_product_title_displayed() == 1

    def test_display_product_price(self, browser):
        inventory_page = InventoryPage(browser)
        product_page = ProductPage(browser)
        common_logic = CommonLogic(browser)
        common_logic.login()
        inventory_page.open_product()
        assert product_page.is_product_price_displayed() == 1

    def test_display_product_description(self, browser):
        inventory_page = InventoryPage(browser)
        product_page = ProductPage(browser)
        common_logic = CommonLogic(browser)
        common_logic.login()
        inventory_page.open_product()
        assert product_page.is_product_description_displayed() == 1

    def test_product_title(self, browser):
        inventory_page = InventoryPage(browser)
        product_page = ProductPage(browser)
        common_logic = CommonLogic(browser)
        common_logic.login()
        product_title_on_inventory_page = inventory_page.get_products_names()
        inventory_page.open_product()
        product_title_on_product_page = product_page.get_product_name()
        assert product_title_on_inventory_page[0] == product_title_on_product_page

    def test_product_price(self, browser):
        inventory_page = InventoryPage(browser)
        product_page = ProductPage(browser)
        common_logic = CommonLogic(browser)
        common_logic.login()
        product_price_on_inventory_page = inventory_page.get_products_prices()
        inventory_page.open_product()
        product_price_on_product_page = product_page.get_product_price()
        assert product_price_on_inventory_page[0] == product_price_on_product_page

    def test_add_product_to_cart_check_counter(self, browser):
        inventory_page = InventoryPage(browser)
        product_page = ProductPage(browser)
        common_logic = CommonLogic(browser)
        common_logic.login()
        inventory_page.open_product()
        product_page.add_product_to_cart()
        assert inventory_page.get_number_of_shopping_cart_counter() == '1'

    def test_add_product_to_cart_display_remove(self, browser):
        inventory_page = InventoryPage(browser)
        product_page = ProductPage(browser)
        common_logic = CommonLogic(browser)
        common_logic.login()
        inventory_page.open_product()
        product_page.add_product_to_cart()
        assert product_page.is_remove_button_present() == 1

    def test_added_product_in_cart(self, browser):
        inventory_page = InventoryPage(browser)
        product_page = ProductPage(browser)
        cart_page = CartPage(browser)
        common_logic = CommonLogic(browser)
        common_logic.login()
        inventory_page.open_product()
        product_name = product_page.get_product_name()
        product_page.add_product_to_cart()
        inventory_page.open_cart()
        assert cart_page.get_added_product_name() == product_name

    def test_remove_product_check_counter(self, browser):
        inventory_page = InventoryPage(browser)
        product_page = ProductPage(browser)
        common_logic = CommonLogic(browser)
        common_logic.login()
        inventory_page.open_product()
        product_page.add_product_to_cart()
        product_page.remove_product()
        assert inventory_page.is_shopping_cart_counter_displayed() == 0

    def test_remove_product_check_display_remove(self, browser):
        inventory_page = InventoryPage(browser)
        product_page = ProductPage(browser)
        common_logic = CommonLogic(browser)
        common_logic.login()
        inventory_page.open_product()
        product_page.add_product_to_cart()
        product_page.remove_product()
        assert product_page.is_remove_button_present() == 0

    def test_back_to_products(self, browser):
        inventory_page = InventoryPage(browser)
        product_page = ProductPage(browser)
        common_logic = CommonLogic(browser)
        common_logic.login()
        inventory_page.open_product()
        product_page.back_to_products()
        assert inventory_page.current_url() == 'https://www.saucedemo.com/inventory.html'
