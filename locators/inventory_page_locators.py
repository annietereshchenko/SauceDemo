from selenium.webdriver.common.by import By


class InventoryPageLocators:

    PRODUCT_TITLE = (By.CLASS_NAME, 'inventory_item_name')
    PRODUCT_PRICE = (By.CLASS_NAME, 'inventory_item_price')
    ADD_BACKPACK_TO_CART = (By.ID, 'add-to-cart-sauce-labs-backpack')
    REMOVE_BACKPACK = (By.ID, 'remove-sauce-labs-backpack')
    CART = (By.CLASS_NAME, 'shopping_cart_link')
    COUNT_OF_ADDED_PRODUCTS = (By.CLASS_NAME, 'shopping_cart_badge')
    SORT = (By.CLASS_NAME, 'product_sort_container')
