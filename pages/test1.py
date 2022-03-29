from selenium.webdriver.common.by import By

link = "http://selenium1py.pythonanywhere.com/en-gb/accounts/login/"

browser.get(link)

def test_should_be_login_url():
    assert "login" in browser.current_url, "Login url is not presented"

def test_should_be_login_form():
    assert browser.find_element(By.CSS_SELECTOR, "#login_form"), "Login form is not presented"

def test_should_be_register_form():
    assert browser.find_element(By.CSS_SELECTOR, "#register_form"), "Register form is not presented"
