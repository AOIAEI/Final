from selenium.webdriver.common.by import By
from .base_page import BasePage

class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

    bascet_form = (By.CSS_SELECTOR, "#add_to_basket_form")

class LoginPageLocators():
    login_form = (By.CSS_SELECTOR, "#login_form")

    register_form = (By.CSS_SELECTOR, "#register_form")

