from pages.base_page import BasePage
from locators.inventory_page_locators import InventoryPageLocators
import logging


class InventoryPage(BasePage):

    def products_logging(self):
        products_title_list = self.find_elements(InventoryPageLocators.PRODUCT_TITLE)
        products_prices_list = self.find_elements(InventoryPageLocators.PRODUCT_PRICE)
        for (name, price) in zip(products_title_list, products_prices_list):
            logging.info(f'Название продукта: {name.text}, цена: {price.text}')

    def get_products_count(self):
        self.products_logging()
        return self.get_count_of_elements(InventoryPageLocators.PRODUCT_TITLE)

    def get_products_names(self):
        return self.get_text_of_elements(InventoryPageLocators.PRODUCT_TITLE)

    def add_product_to_cart(self):
        self.find_element(InventoryPageLocators.ADD_BACKPACK_TO_CART).click()

    def get_products_prices(self):
        cast_products_prices_list = []
        products_prices_list = self.get_text_of_elements(InventoryPageLocators.PRODUCT_PRICE)
        for product in products_prices_list:
            # здесь можно было обойтись replace('$', ''), но вдруг там будут
            # пробелы, или другая валюта, или еще что-нибудь
            price = ''.join(filter(lambda c: c.isdigit() or c == '.', product))
            cast_products_prices_list.append(float(price))
        return cast_products_prices_list

    def get_number_of_shopping_cart_counter(self):
        return self.get_text_of_element(InventoryPageLocators.COUNT_OF_ADDED_PRODUCTS)

    def is_shopping_cart_counter_displayed(self):
        return self.is_element_present(*InventoryPageLocators.COUNT_OF_ADDED_PRODUCTS)

    def is_remove_button_present(self):
        return self.is_element_present(*InventoryPageLocators.REMOVE_BACKPACK)

    def open_cart(self):
        self.find_element(InventoryPageLocators.CART).click()

    def remove_product(self):
        self.find_element(InventoryPageLocators.REMOVE_BACKPACK).click()

    def select_sorting_type(self, value):
        self.select(InventoryPageLocators.SORT, value)

    def check_names_sorting(self, reverse):
        product_names = self.get_products_names()
        sorted_product_names = sorted(product_names, reverse=reverse)
        for product, sorted_product in zip(product_names, sorted_product_names):
            if not product == sorted_product:
                return False
        return True

    def check_prices_sorting(self, reverse):
        product_prices = self.get_products_prices()
        sorted_product_prices = sorted(product_prices, reverse=reverse)
        for product, sorted_product in zip(product_prices, sorted_product_prices):
            if not product == sorted_product:
                return False
        return True

    def open_product(self):
        self.find_element(InventoryPageLocators.PRODUCT_TITLE).click()
