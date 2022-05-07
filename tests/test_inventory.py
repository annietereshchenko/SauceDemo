import pytest
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.common_logic import CommonLogic


class TestInventory:

    @pytest.mark.parametrize(
        'product_index, expected_title',
        [(0, 'Sauce Labs Backpack'),
         (1, 'Sauce Labs Bike Light'),
         (2, 'Sauce Labs Bolt T-Shirt'),
         (3, 'Sauce Labs Fleece Jacket'),
         (4, 'Sauce Labs Onesie'),
         (5, 'Test.allTheThings() T-Shirt (Red)')])
    def test_product_title(self, product_index, expected_title, browser):
        inventory_page = InventoryPage(browser)
        common_logic = CommonLogic(browser)
        common_logic.login()
        product_names_list = inventory_page.get_products_names()
        assert product_names_list[product_index] == expected_title

    def test_add_product_to_cart(self, browser):
        inventory_page = InventoryPage(browser)
        common_logic = CommonLogic(browser)
        common_logic.login()
        inventory_page.add_product_to_cart()
        assert inventory_page.get_number_of_shopping_cart_counter() == '1'
        assert inventory_page.is_remove_button_present() == 1

    def test_added_product_in_cart(self, browser):
        inventory_page = InventoryPage(browser)
        cart_page = CartPage(browser)
        common_logic = CommonLogic(browser)
        common_logic.login()
        product_name = inventory_page.get_products_names()
        inventory_page.add_product_to_cart()
        inventory_page.open_cart()
        assert cart_page.get_added_product_name() == product_name[0]

    def test_remove_product(self, browser):
        inventory_page = InventoryPage(browser)
        common_logic = CommonLogic(browser)
        common_logic.login()
        inventory_page.add_product_to_cart()
        inventory_page.remove_product()
        assert inventory_page.is_remove_button_present() == 0
        assert inventory_page.is_shopping_cart_counter_displayed() == 0

    @pytest.mark.parametrize('sorting_type, reverse, expected_sorting', [('az', False, True), ('za', True, True)])
    def test_product_sorting_by_names(self, sorting_type, reverse, expected_sorting, browser):
        inventory_page = InventoryPage(browser)
        common_logic = CommonLogic(browser)
        common_logic.login()
        inventory_page.select_sorting_type(value=sorting_type)
        assert inventory_page.check_names_sorting(reverse=reverse) is expected_sorting

    @pytest.mark.parametrize('sorting_type, reverse, expected_sorting', [('lohi', False, True), ('hilo', True, True)])
    def test_product_sorting_by_prices(self, sorting_type, reverse, expected_sorting, browser):
        inventory_page = InventoryPage(browser)
        common_logic = CommonLogic(browser)
        common_logic.login()
        inventory_page.select_sorting_type(value=sorting_type)
        assert inventory_page.check_prices_sorting(reverse=reverse) is expected_sorting
