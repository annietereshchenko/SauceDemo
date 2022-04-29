import pytest
from selenium import webdriver


@pytest.fixture(scope="function")
def browser():
    browser = webdriver.Chrome("C:/Users/Admin/PycharmProjects/TMS05_HW/chromedriver")
    browser.maximize_window()
    browser.implicitly_wait(10)
    yield browser
    browser.quit()
