from pages.base_page import BasePage
from locators.login_page_locators import LoginPageLocators


class LoginPage(BasePage):

    def enter_name(self, name):
        self.send_keys(LoginPageLocators.USERNAME, name)

    def enter_password(self, password):
        self.send_keys(LoginPageLocators.PASSWORD, password)

    def click_on_login(self):
        self.find_element(LoginPageLocators.LOGIN_BUTTON).click()
