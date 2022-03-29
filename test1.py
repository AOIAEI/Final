
def test_guest_should_see_login_page(browser):
    page = LoginPage(browser, link)
    page.open()
    page.should_be_login_page()


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url(self)
        self.should_be_login_form()
        self.should_be_register_form()


class LoginPageLocators():
    def should_be_login_url(self):
        assert "login" in current_url, "Login url is not presented"

    def should_be_login_form(self):
        assert self.is_element_present(By.CSS_SELECTOR, "#login_form"), "Login form is not presented"

    def should_be_register_form(self):
        assert self.is_element_present(By.CSS_SELECTOR, "#register_form"), "Register form is not presented"
