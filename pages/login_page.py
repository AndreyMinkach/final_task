import pytest

from pages.locators import LoginPageLocators
from pages.main_page import MainPage


class LoginPage(MainPage):

    def register_new_user(self, email, password):
        self.browser.find_element(*LoginPageLocators.LOGIN_FORM).click()
        self.browser.find_element(*LoginPageLocators.REGISTRATION_EMAIL_ADDRESS).send_keys(email)
        self.browser.find_element(*LoginPageLocators.REGISTRATION_PASSWORD).send_keys(password)
        self.browser.find_element(*LoginPageLocators.REGISTRATION_CONFIRM_PASSWORD).send_keys(password)
        self.browser.find_element(*LoginPageLocators.CONFIRM_BUTTON).click()

    @pytest.fixture(scope="function", autouse=True)
    def setup(self):
        self.go_to_login_page()
        self.register_new_user()
        self.should_be_authorized_user()

    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        # реализуйте проверку на корректный url адрес
        assert self.browser.current_url in self.url, "past url not in current url"

    def should_be_login_form(self):
        # реализуйте проверку, что есть форма логина
        assert self.is_element_present(*LoginPageLocators.LOGIN_BUTTON), "Cant find login button"

    def should_be_register_form(self):
        # реализуйте проверку, что есть форма регистрации на странице
        assert self.is_element_present(*LoginPageLocators.REGISTER_BUTTON), "Cant find register button"
