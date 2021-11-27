import allure
from pages.base_page import BasePage
from pages.locators import LoginPageLocators
from constants import LOGIN_PAGE_URL
import random

path = LOGIN_PAGE_URL


class LoginPage(BasePage):
    def should_be_login_page(self):
        #self.should_be_login_url()
        self.should_be_click_myacc()
        self.should_be_login_form()
        self.should_be_login_url
        #self.should_be_register_form()

    def should_be_click_myacc(self):
        self.click(*LoginPageLocators.LOGIN_PAGE_URL)

    def should_be_login_url(self):
        current_url = self._browser.current_url
        assert current_url == "http://practice.automationtesting.in/my-account/"

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not presented"

    def enter_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_EMAIL_FIELD), "EMAIL field is not presented"
        assert self.is_element_present(*LoginPageLocators.LOGIN_PASSWORD_FIELD), "Password field is not presented"
        self.write_field(*LoginPageLocators.LOGIN_EMAIL_FIELD, "ronyacsrf@mail.ru")
        self.write_field(*LoginPageLocators.LOGIN_PASSWORD_FIELD, "ronyacsrf@mail.ru")
        self.click(*LoginPageLocators.LOGIN_BUTTON)

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTRATION_FORM), "Registration form is not presented"


    def register_user(self):
        self.write_field(*LoginPageLocators.REGISTRATION_EMAIL_FIELD, "roniamincsrf@mail.ru")
        self.write_field(*LoginPageLocators.REGISTRATION_PASSWORD_FIELD, "roniamincsrf@mail.ru")
        self.click(*LoginPageLocators.REGISTRATION_BUTTON)

    def register_new_user(self, i_password='Testpass1123'):
        self._browser.find_element(*LoginPageLocators.REGISTRATION_EMAIL_FIELD).send_keys(str(random.getrandbits(25)) +
                                                                                         "@fake-email.org")
        self.write_field(*LoginPageLocators.REGISTRATION_PASSWORD_FIELD, i_password)
        self.write_field(*LoginPageLocators.REGISTRATION_CONFIRM_PASSWORD_FIELD, i_password)
        self.click(*LoginPageLocators.REGISTRATION_BUTTON)
        assert self.is_element_present(*LoginPageLocators.REGISTRATION_COMPLETE_MESSAGE), \
            "Registration message is not presented"

    @allure.step('Register new user with not valid email')
    def register_new_user_with_not_valid_email(self, i_email='not-valid-email.org', i_password='Test-pass1123'):
        self.write_field(*LoginPageLocators.REGISTRATION_EMAIL_FIELD, i_email)
        self.write_field(*LoginPageLocators.REGISTRATION_PASSWORD_FIELD, i_password)
        self.write_field(*LoginPageLocators.REGISTRATION_CONFIRM_PASSWORD_FIELD, i_password)
        self.click(*LoginPageLocators.REGISTRATION_BUTTON)
        assert not self.is_element_present(*LoginPageLocators.REGISTRATION_COMPLETE_MESSAGE), \
            "Whoops! Registration message presented"
