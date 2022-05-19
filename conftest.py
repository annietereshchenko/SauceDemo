import pytest
from selenium import webdriver


@pytest.fixture()
def browser():
    browser = webdriver.Chrome("C:/Users/Admin/PycharmProjects/SauceDemo/chromedriver")
    browser.maximize_window()
    browser.implicitly_wait(5)
    browser.get('https://www.saucedemo.com/')
    yield browser
    browser.quit()


@pytest.fixture()
def browse_dc():
    browser = webdriver.Chrome("C:/Users/Admin/PycharmProjects/TMS05_HW/chromedriver")
    browser.maximize_window()
    browser.implicitly_wait(5)
    browser.get('http://the-internet.herokuapp.com/dynamic_controls')
    yield browser
    browser.quit()
