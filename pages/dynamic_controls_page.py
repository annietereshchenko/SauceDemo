from pages.base import BasePage
from locators.dynamic_controls_page_locators import DynamicControlsPageLocators
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class DynamicControlsPage(BasePage):

    def __init__(self, browser, url=''):
        if not url:
            url = "http://the-internet.herokuapp.com/dynamic_controls"

        super().__init__(browser, url)

    def wait_for_visibility_of_element(self, *element):
        WebDriverWait(self.browser, 5).until(
            EC.visibility_of(self.browser.find_element(*element)))

    def remove_checkbox(self):
        self.browser.find_element(*DynamicControlsPageLocators.REMOVE_BUTTON).click()
        self.wait_for_visibility_of_element(*DynamicControlsPageLocators.MESSAGE)

    def is_element_present(self):
        return self.browser.find_elements(*DynamicControlsPageLocators.CHECKBOX)

    def is_element_disabled(self):
        return self.browser.find_element(*DynamicControlsPageLocators.INPUT_FIELD).get_property('disabled')

    def click_on_button(self):
        self.browser.find_element(*DynamicControlsPageLocators.ENABLE_BUTTON).click()
        self.wait_for_visibility_of_element(*DynamicControlsPageLocators.MESSAGE)
