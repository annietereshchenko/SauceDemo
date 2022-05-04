from selenium.webdriver.support.select import Select
from pages.base import BasePage
from locators.login_page_locators import LoginPageLocators
from locators.inventory_page_locators import InventoryPageLocators
import logging


class LoginPage(BasePage):

    def __init__(self, browser, url=''):
        if not url:
            url = "https://www.saucedemo.com/"

        super().__init__(browser, url)

    def login(self):
        self.browser.find_element(*LoginPageLocators.USERNAME).send_keys('standard_user')
        self.browser.find_element(*LoginPageLocators.PASSWORD).send_keys('secret_sauce')
        self.browser.find_element(*LoginPageLocators.LOGIN_BUTTON).click()

    def get_products_count(self):
        products_title_list = self.browser.find_elements(*InventoryPageLocators.PRODUCT_TITLE)
        products_prices_list = self.browser.find_elements(*InventoryPageLocators.PRODUCT_PRICE)
        for (name, price) in zip(products_title_list, products_prices_list):
            logging.info(f'Название продукта: {name.text}, цена: {price.text}')
        return len(products_title_list)

    def get_products_names(self):
        products_names_list = []
        products_list = self.browser.find_elements(*InventoryPageLocators.PRODUCT_TITLE)
        for product in products_list:
            products_names_list.append(product.text)
        return products_names_list

    def add_product_to_cart(self):
        self.browser.find_element(*InventoryPageLocators.ADD_BACKPACK_TO_CART).click()

    def get_products_prices(self):
        products_prices_list = []
        products_list = self.browser.find_elements(*InventoryPageLocators.PRODUCT_PRICE)
        for product in products_list:
            price = ''.join(filter(lambda c: c.isdigit() or c == '.', product.text))
            products_prices_list.append(float(price))
        return products_prices_list

    def get_count_of_added_products(self):
        return self.browser.find_element(*InventoryPageLocators.COUNT_OF_ADDED_PRODUCTS).text

    def is_remove_button_present(self):
        return len(self.browser.find_elements(*InventoryPageLocators.REMOVE_BACKPACK))

    def open_cart(self):
        self.browser.find_element(*InventoryPageLocators.CART).click()

    def get_added_product_name(self):
        return self.browser.find_element(*InventoryPageLocators.PRODUCT_TITLE).text

    def remove_product(self):
        self.browser.find_element(*InventoryPageLocators.REMOVE_BACKPACK).click()

    def select_sorting_type(self, value):
        Select(self.browser.find_element(*InventoryPageLocators.SORT)).select_by_value(value)

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
