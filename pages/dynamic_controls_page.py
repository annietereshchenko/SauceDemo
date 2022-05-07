from pages.base_page import BasePage
from locators.dynamic_controls_page_locators import DynamicControlsPageLocators


class DynamicControlsPage(BasePage):

    def remove_checkbox(self):
        self.find_element(DynamicControlsPageLocators.REMOVE_BUTTON).click()
        self.wait_for_visibility_of_element(DynamicControlsPageLocators.MESSAGE)

    def is_checkbox_present(self):
        return self.is_element_present(*DynamicControlsPageLocators.CHECKBOX)

    def is_element_disabled(self):
        return self.find_element(DynamicControlsPageLocators.INPUT_FIELD).get_property('disabled')

    def click_on_enable_button(self):
        self.find_element(DynamicControlsPageLocators.ENABLE_BUTTON).click()
        self.wait_for_visibility_of_element(DynamicControlsPageLocators.MESSAGE)
