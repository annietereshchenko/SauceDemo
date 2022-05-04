import pytest
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage


class TestInventory:

    @pytest.mark.parametrize('product_index, expected_title',
                             [(0, 'Sauce Labs Backpack'),
                              (1, 'Sauce Labs Bike Light'),
                              (2, 'Sauce Labs Bolt T-Shirt'),
                              (3, 'Sauce Labs Fleece Jacket'),
                              (4, 'Sauce Labs Onesie'),
                              (5, 'Test.allTheThings() T-Shirt (Red)')])
    def test_product_title(self, product_index, expected_title, browser):
        login_page = LoginPage(browser)
        inventory_page = InventoryPage(browser)
        login_page.open()
        login_page.login()
        product_names_list = inventory_page.get_products_names()
        assert product_names_list[product_index] == expected_title

    def test_add_product_to_cart(self, browser):
        login_page = LoginPage(browser)
        inventory_page = InventoryPage(browser)
        login_page.open()
        login_page.login()
        inventory_page.add_product_to_cart()
        assert inventory_page.get_count_of_added_products() == '1'
        assert inventory_page.is_remove_button_present() == 1

    def test_added_product_in_cart(self, browser):
        login_page = LoginPage(browser)
        inventory_page = InventoryPage(browser)
        login_page.open()
        login_page.login()
        inventory_page.add_product_to_cart()
        inventory_page.open_cart()
        assert inventory_page.get_added_product_name() == 'Sauce Labs Backpack'

    def test_remove_product(self, browser):
        login_page = LoginPage(browser)
        inventory_page = InventoryPage(browser)
        login_page.open()
        login_page.login()
        inventory_page.add_product_to_cart()
        inventory_page.remove_product()
        assert inventory_page.is_remove_button_present() == 0

    def test_a_to_z_sorting(self, browser):
        login_page = LoginPage(browser)
        inventory_page = InventoryPage(browser)
        login_page.open()
        login_page.login()
        inventory_page.select_sorting_type(value='az')
        assert inventory_page.check_names_sorting(reverse=False) is True

    def test_z_to_a_sorting(self, browser):
        login_page = LoginPage(browser)
        inventory_page = InventoryPage(browser)
        login_page.open()
        login_page.login()
        inventory_page.select_sorting_type(value='za')
        assert inventory_page.check_names_sorting(reverse=True) is True

    # @pytest.mark.parametrize('sorting_type, reverse, expected_result', [('az', False, True), ('za', True, True)])
    # def test(self, sorting_type, reverse, expected_result, browser):
    #     login_page = LoginPage(browser)
    #     inventory_page = InventoryPage(browser)
    #     login_page.open()
    #     login_page.login()
    #     inventory_page.select_sorting_type(value=sorting_type)
    #     assert inventory_page.check_names_sorting(reverse=reverse) is expected_result

    def test_low_to_high_sorting(self, browser):
        login_page = LoginPage(browser)
        inventory_page = InventoryPage(browser)
        login_page.open()
        login_page.login()
        inventory_page.select_sorting_type(value='lohi')
        assert inventory_page.check_prices_sorting(reverse=False) is True

    def test_high_to_low_sorting(self, browser):
        login_page = LoginPage(browser)
        inventory_page = InventoryPage(browser)
        login_page.open()
        login_page.login()
        inventory_page.select_sorting_type(value='hilo')
        assert inventory_page.check_prices_sorting(reverse=True) is True

    # @pytest.mark.parametrize('sorting_type, reverse, expected_result', [('lohi', False, True), ('hilo', True, True)])
    # def test(self, sorting_type, reverse, expected_result, browser):
    #     login_page = LoginPage(browser)
    #     inventory_page = InventoryPage(browser)
    #     login_page.open()
    #     login_page.login()
    #     inventory_page.select_sorting_type(value=sorting_type)
    #     assert inventory_page.check_prices_sorting(reverse=reverse) is expected_result
