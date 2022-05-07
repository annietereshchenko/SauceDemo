from pages.base_page import BasePage
from locators.product_page_locators import ProductPageLocators


class ProductPage(BasePage):

    def is_product_icon_displayed(self):
        return self.is_element_present(*ProductPageLocators.PRODUCT_ICON)

    def is_product_title_displayed(self):
        return self.is_element_present(*ProductPageLocators.PRODUCT_TITLE)

    def is_product_price_displayed(self):
        return self.is_element_present(*ProductPageLocators.PRODUCT_ICON)

    def is_product_description_displayed(self):
        return self.is_element_present(*ProductPageLocators.PRODUCT_ICON)

    def get_product_name(self):
        return self.get_text_of_element(ProductPageLocators.PRODUCT_TITLE)

    def get_product_price(self):
        product_price = self.get_text_of_element(ProductPageLocators.PRODUCT_PRICE)
        #cast_product_price = product_price.replace('$', '')
        cast_product_price = ''.join(filter(lambda c: c.isdigit() or c == '.', product_price))
        return float(cast_product_price)

    def add_product_to_cart(self):
        self.find_element(ProductPageLocators.ADD_BACKPACK_TO_CART).click()

    def is_remove_button_present(self):
        return self.is_element_present(*ProductPageLocators.REMOVE_BACKPACK)

    def remove_product(self):
        self.find_element(ProductPageLocators.REMOVE_BACKPACK).click()

    def back_to_products(self):
        self.find_element(ProductPageLocators.BACK_TO_PRODUCTS).click()
