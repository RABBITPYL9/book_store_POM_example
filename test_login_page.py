import pytest
from pages.locators import LoginPageLocators
from pages.login_page import LoginPage, path
from constants import BASE_URL

@pytest.mark.runik
def test_guest_can_go_to_login_page(browser):
    #page = LoginPage(browser, BASE_URL+path)
    page = LoginPage(browser, BASE_URL)
    page.open()
    page.should_be_login_page()

@pytest.mark.runik
def test_enter_login_data(browser):
    page = LoginPage(browser, BASE_URL)
    page.open()
    page.should_be_login_page()
    page.enter_login_form()

@pytest.mark.runik
def test_reg_user(browser):
    page = LoginPage(browser, BASE_URL)
    page.open()
    page.should_be_login_page()
    page.register_user()


