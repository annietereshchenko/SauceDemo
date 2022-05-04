from selenium.webdriver.common.by import By


class ProductPageLocators:

    PRODUCT_TITLE = (By.CLASS_NAME, 'inventory_details_name')
    PRODUCT_PRICE = (By.CLASS_NAME, 'inventory_details_price')
    ADD_BACKPACK_TO_CART = (By.ID, 'add-to-cart-sauce-labs-backpack')
    REMOVE_BACKPACK = (By.ID, 'remove-sauce-labs-backpack')
    PRODUCT_DESCRIPTION = (By.CLASS_NAME, 'inventory_details_desc')
    PRODUCT_ICON = (By.CLASS_NAME, 'inventory_details_img')
    BACK_TO_PRODUCTS = (By.ID, 'back-to-products')
