from selenium.webdriver.common.by import By


class LoginPageLocators:

    LOGIN_LOGO = (By.CLASS_NAME, 'login_logo')
    USERNAME = (By.ID, 'user-name')
    PASSWORD = (By.ID, 'password')
    LOGIN_BUTTON = (By.ID, 'login-button')
