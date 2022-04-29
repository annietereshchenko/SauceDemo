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
