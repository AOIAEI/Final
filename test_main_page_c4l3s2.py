from .pages.main_page import MainPage
from .pages.base_page import BasePage
from .pages.login_page import LoginPage
from selenium.common.exceptions import NoSuchElementException
import time

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"

def test_guest_can_go_to_buy_item(browser):
    page = MainPage(browser, link)  
    page.open()  
    item_name = browser.find_element_by_tag_name("h1").text
    item_price = browser.find_element_by_class_name("price_color").text
    time.sleep(2)
    page.go_to_buy_page()  
    time.sleep(2)                  
    page.solve_quiz_and_get_code()
    time.sleep(5) 
    page.check_item_name(item_name)
    page.check_item_price(item_price)



