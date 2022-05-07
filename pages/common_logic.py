from pages.login_page import LoginPage


class CommonLogic(LoginPage):

    def login(self):
        self.enter_name('standard_user')
        self.enter_password('secret_sauce')
        self.click_on_login()
