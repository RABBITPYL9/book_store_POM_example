import pytest
from pages.main_page import MainPage
from constants import BASE_URL

@pytest.mark.runik
def test_guest_can_go_to_login_page(browser):
    page = MainPage(browser, BASE_URL)
    page.open()
    page.test_add_comment()

