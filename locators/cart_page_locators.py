from selenium.webdriver.common.by import By


class CartPageLocators:

    QUANTITY = (By.CLASS_NAME, 'cart_quantity')
    REMOVE_BACKPACK = (By.ID, 'remove-sauce-labs-backpack')
    CONTINUE_SHOPPING = (By.ID, 'continue-shopping')
    CHECKOUT = (By.ID, 'checkout')
    PRODUCT_TITLE = (By.CLASS_NAME, 'inventory_item_name')
    PASSWORD = (By.ID, 'password')
    LOGIN_BUTTON = (By.ID, 'login-button')
