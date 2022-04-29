from selenium.webdriver.common.by import By


class InventoryPageLocators:

    PRODUCT_TITLE = (By.CLASS_NAME, 'inventory_item_name')
    PRODUCT_PRICE = (By.CLASS_NAME, 'inventory_item_price')
