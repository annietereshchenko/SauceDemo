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

        username = self.browser.find_element(*LoginPageLocators.USERNAME)
        username.send_keys('standard_user')
        password = self.browser.find_element(*LoginPageLocators.PASSWORD)
        password.send_keys('secret_sauce')
        login_button = self.browser.find_element(*LoginPageLocators.LOGIN_BUTTON)
        login_button.click()

    def get_products_count(self):
        products_title = self.browser.find_elements(*InventoryPageLocators.PRODUCT_TITLE)
        products_prices = self.browser.find_elements(*InventoryPageLocators.PRODUCT_PRICE)
        for (name, price) in zip(products_title, products_prices):
            logging.info(f'Название продукта: {name.text}, цена: {price.text}')
        return len(products_title)
