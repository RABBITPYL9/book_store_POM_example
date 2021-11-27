import pytest
from pages.locators import ProductPageLocators
from pages.shop_page import ProductPage, path
from constants import BASE_URL
import time

#@pytest.mark.runik
def test_view_product(browser):
    page = ProductPage(browser, BASE_URL)
    page.open()
    page.move_to_product_view()

#@pytest.mark.runik
def test_add_to_backet(browser):
    page = ProductPage(browser, BASE_URL)
    page.open()
    page.move_to_product_view()
    page.tov_add_to_cart()


    
