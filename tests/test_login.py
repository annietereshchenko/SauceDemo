from pages.login_page import LoginPage


class TestLogin:

    def test_login(self, browser):
        page = LoginPage(browser)
        page.open()
        page.login()
        assert page.current_url() == 'https://www.saucedemo.com/inventory.html'
        assert page.get_products_count() == 6
