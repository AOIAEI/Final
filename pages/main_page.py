from .base_page import BasePage
from .locators import MainPageLocators
from selenium.webdriver.common.by import By

class MainPage(BasePage):
    def go_to_login_page(self):
        login_link = self.browser.find_element(*MainPageLocators.LOGIN_LINK)
        login_link.click() 

    def should_be_login_link(self):
        assert self.is_element_present(*MainPageLocators.LOGIN_LINK), "Login link is not presented"

    def should_be_login_link(self):
        assert self.is_element_present(*MainPageLocators.LOGIN_LINK), "Login link is not presented"

    def go_to_buy_page(self):
        login_link = self.browser.find_element(*MainPageLocators.bascet_form)
        login_link.click() 

    def check_item_name(self, name):
        item_name = self.browser.find_element(By.XPATH, "//article/div[1]/div[2]/h1").text
        assert item_name == name, "Name is wrong"

    def check_item_price(self, price):
        item_price = self.browser.find_element(By.XPATH, "//article/div[1]/div[2]/p[1]").text
        assert item_price == price, "Price is wrong"