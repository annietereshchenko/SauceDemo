from pages.base_page import BasePage
from locators.cart_page_locators import CartPageLocators


class CartPage(BasePage):

    def get_added_product_name(self):
        return self.get_text_of_element(CartPageLocators.PRODUCT_TITLE)

