from selenium.webdriver.common.by import By


class DynamicControlsPageLocators:

    CHECKBOX = (By.ID, 'checkbox')
    REMOVE_BUTTON = (By.CSS_SELECTOR, '#checkbox-example > button')
    MESSAGE = (By.ID, 'message')
    INPUT_FIELD = (By.CSS_SELECTOR, '#input-example > input')
    ENABLE_BUTTON = (By.CSS_SELECTOR, '#input-example > button')
