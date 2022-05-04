from pages.base import BasePage
from locators.product_page_locators import ProductPageLocators


class ProductPage(BasePage):

    def is_product_icon_displayed(self):
        return len(self.browser.find_elements(*ProductPageLocators.PRODUCT_ICON))

    def is_product_title_displayed(self):
        return len(self.browser.find_elements(*ProductPageLocators.PRODUCT_TITLE))

    def is_product_price_displayed(self):
        return len(self.browser.find_elements(*ProductPageLocators.PRODUCT_ICON))

    def is_product_description_displayed(self):
        return len(self.browser.find_elements(*ProductPageLocators.PRODUCT_ICON))

    def get_product_name(self):
        return self.browser.find_element(*ProductPageLocators.PRODUCT_TITLE).text

    def get_product_price(self):
        product_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE)
        product_price_f = ''.join(filter(lambda c: c.isdigit() or c == '.', product_price.text))
        return float(product_price_f)

    def add_product_to_cart(self):
        self.browser.find_element(*ProductPageLocators.ADD_BACKPACK_TO_CART).click()

    def is_remove_button_present(self):
        return len(self.browser.find_elements(*ProductPageLocators.REMOVE_BACKPACK))

    def remove_product(self):
        self.browser.find_element(*ProductPageLocators.REMOVE_BACKPACK).click()

    def back_to_products(self):
        self.browser.find_element(*ProductPageLocators.BACK_TO_PRODUCTS).click()
