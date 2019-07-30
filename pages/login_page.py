from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        link = self.browser.current_url
        assert "login" in link, "The link does not contain the word login"

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Maybe not LOGIN_FORM"
        assert True

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "Maybe not REGISTER_FORM"
        assert True

    def register_new_user(self, email, password):
        self.browser.find_element(*LoginPageLocators.REG_EMAIL).send_keys(email)
        self.browser.find_element(*LoginPageLocators.REG_PASSWORD).send_keys(password)
        self.browser.find_element(*LoginPageLocators.REG_CONFIRM_PASSWORD).send_keys(password)
        self.browser.find_element(*LoginPageLocators.REG_BUTTON).click()