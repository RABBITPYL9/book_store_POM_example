import random
from pages.locators import LoginPageLocators
from pages.login_page import LoginPage
from constants import PASSWORD


def setup_user_register(browser):
    login_page = LoginPage(browser, "http://practice.automationtesting.in/")
    login_page.open()
    login_page.register_new_user()
