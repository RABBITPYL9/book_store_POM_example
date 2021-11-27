import allure
from pages.base_page import BasePage
from pages.locators import MainPageLocators
import time


class MainPage(BasePage):
    _base_path = None

    def go_to_login_page(self):
        self.click(*MainPageLocators.LOGIN_LINK), "Login link is not presented"

    def should_be_login_link(self):
        assert self.is_element_present(*MainPageLocators.LOGIN_LINK), "Login link is not presented"

    def test_add_comment(self):
        self._browser.execute_script("window.scrollBy(0, 600);")
        assert self.is_element_present(*MainPageLocators.TOV_LINK), "TOV LINK field is not presented"
        self.click(*MainPageLocators.TOV_LINK), "TOV link is not presented"
        assert self.is_element_present(*MainPageLocators.REVIEW_LINK), "REVIEW LINK field is not presented"
        #self.click(*MainPageLocators.TOV_LINK), "TOV link is not presented"
        self.click(*MainPageLocators.REVIEW_LINK), "REVIEW link is not presented"
        self.click(*MainPageLocators.CLICK_RATING_MAX), "Rating is not presented"
        self.write_field(*MainPageLocators.FIELD_COMMENT, "RONYAYSPESNHIYXXX")
        self.write_field(*MainPageLocators.FIELD_COMMENT_AUTHOR, "RONIXXXXX317")
        self.write_field(*MainPageLocators.FIELD_COMMENT_EMAIL, "RONbKA317Xcsrf@mail.ru")
        self.click(*MainPageLocators.BTN_COMMENT_SUBMIT)
        assert self.is_element_present(*MainPageLocators.MSG_COMMENT_APPROVE), "MSG LINK field is not presented"
