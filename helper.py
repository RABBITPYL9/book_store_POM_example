import random
from pages.locators import LoginPageLocators
from pages.login_page import LoginPage
from constants import PASSWORD


def setup_user_register(browser):
    login_page = LoginPage(browser, "http://practice.automationtesting.in/")
    login_page.open()
    login_page.register_new_user()


# def register_new_user(self, i_password=PASSWORD):
#         self.browser.find_element(*LoginPageLocators.REGISTRATION_EMAIL_FIELD).send_keys(str(random.getrandbits(25)) +
#                                                                                          "@fake-email.org")
#         self.write_field(*LoginPageLocators.REGISTRATION_PASSWORD_FIELD, i_password)
#         self.write_field(*LoginPageLocators.REGISTRATION_CONFIRM_PASSWORD_FIELD, i_password)
#         self.click(*LoginPageLocators.REGISTRATION_BUTTON)
