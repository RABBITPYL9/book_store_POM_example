import allure
from conftest import browser
from pages.base_page import BasePage
from pages.locators import LoginPageLocators, ProductPageLocators
from constants import LOGIN_PAGE_URL
import random
from selenium.webdriver.common.by import By

path = LOGIN_PAGE_URL


class ProductPage(BasePage):
    def shop_product_page(self):
        self.move_to_product_view()

    @allure.step('Move to shop menu')
    def click_on_shop_menu(self):
        self.click(*ProductPageLocators.MOVE_TO_SHOP_PAGE)

    @allure.step('Go to page of page')
    def move_to_product_view(self):
        self.click_on_shop_menu()
        self.click(*ProductPageLocators.VIEW_PRODUCT_PAGE)
        #assert "HTML5 Forms – Automation Practice Site" in browser.title, "Находимся на странице другой книги" #проверяем что мы на странице нужной книге
        assert self.title_assert("HTML5 Forms – Automation Practice Site"), "title text is not presented"
    
    @allure.step('Check tov in cart')
    def tov_add_to_cart(self):
        self.click(*ProductPageLocators.CHECKOUT_BTN)
        self.is_element_present(*ProductPageLocators.MSG_ADDED_TOV)
        self.click(*ProductPageLocators.CHECKOUT_PAGE)
        self.is_element_present(*ProductPageLocators.COUNT_TOV_IN_CHECKOUT)
