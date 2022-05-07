from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:

    def __init__(self, browser):
        self.browser = browser

    def current_url(self):
        return self.browser.current_url

    def find_element(self, locator, timeout=10):
        element = WebDriverWait(self.browser, timeout).until(EC.presence_of_element_located(locator))
        return element

    def find_elements(self, locator, timeout=10):
        elements = WebDriverWait(self.browser, timeout).until(EC.presence_of_all_elements_located(locator))
        return elements

    def send_keys(self, locator, keys):
        element = self.find_element(locator)
        element.send_keys(keys)

    def wait_for_visibility_of_element(self, locator):
        WebDriverWait(self.browser, 10).until(
            EC.visibility_of(self.find_element(locator)))

    def is_element_present(self, *locator):
        return len(self.browser.find_elements(*locator))

    def get_count_of_elements(self, locator):
        elements = self.find_elements(locator)
        return len(elements)

    def get_text_of_elements(self, locator):
        elements = self.find_elements(locator)
        result = []
        for element in elements:
            result.append(element.text)
        return result

    def get_text_of_element(self, locator):
        element = self.find_element(locator)
        return element.text

    def select(self, locator, value):
        Select(self.find_element(locator)).select_by_value(value)
