from pages.base import BasePage
from locators.login_page_locators import LoginPageLocators


class LoginPage(BasePage):

    def login(self):
        self.browser.find_element(*LoginPageLocators.USERNAME).send_keys('standard_user')
        self.browser.find_element(*LoginPageLocators.PASSWORD).send_keys('secret_sauce')
        self.browser.find_element(*LoginPageLocators.LOGIN_BUTTON).click()
