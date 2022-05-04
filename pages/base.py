class BasePage:

    def __init__(self, browser, timeout=10):
        self.browser = browser
        self.browser.implicitly_wait(timeout)

    def current_url(self):
        return self.browser.current_url
