from selenium.webdriver.common.by import By


class BasePageLocators():
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    TOV_LINK = (By.CSS_SELECTOR, "#text-22-sub_row_1-0-2-0-0 > div > ul >li > a:nth-child(1)")
    REVIEW_LINK = (By.CSS_SELECTOR, "[class='reviews_tab'] a")
    CLICK_RATING_MAX = (By.CSS_SELECTOR, "[class='star-5']")
    FIELD_COMMENT = (By.ID, "comment")
    FIELD_COMMENT_AUTHOR = (By.ID, "author")
    FIELD_COMMENT_EMAIL = (By.ID, "email")
    BTN_COMMENT_SUBMIT = (By.ID, "submit")
    MSG_COMMENT_APPROVE = (By.XPATH, "//*[text()='Your comment is awaiting approval']")


class LoginPageLocators():
    LOGIN_PAGE_URL = (By.CSS_SELECTOR, "#menu-item-50 a")
    LOGIN_FORM = (By.CSS_SELECTOR, "[class='login']")
    LOGIN_EMAIL_FIELD = (By.ID, "username")
    LOGIN_PASSWORD_FIELD = (By.ID, "password")
    LOGIN_BUTTON = (By.CSS_SELECTOR, "[value='Login']")
    LOGIN_COMPLETE_MESSAGE = (By.CSS_SELECTOR, "[class='woocommerce-MyAccount-content']")
    REGISTRATION_FORM = (By.CSS_SELECTOR, "[class='register']")
    REGISTRATION_EMAIL_FIELD = (By.ID, "reg_email")
    REGISTRATION_PASSWORD_FIELD = (By.ID, "reg_password")
    REGISTRATION_BUTTON = (By.CSS_SELECTOR, "[value='Register']")


class ProductPageLocators():
    LOGIN_PAGE_URL = (By.CSS_SELECTOR, "#login_link")
    ADD_TO_BASKET_BUTTON = (By.XPATH, "//form[@id='add_to_basket_form']//button[contains(@type,'submit')]")
    SAVE_REVIEW_BUTTON = (By.XPATH, "//form[@id='add_review_form']//button[contains(@type,'submit')]")
    MOVE_TO_SHOP_PAGE = (By.CSS_SELECTOR, "#menu-item-40 a")
    VIEW_PRODUCT_PAGE = (By.CSS_SELECTOR, "[alt='Mastering HTML5 Forms']")
    BOOK_TO_CART = (By.CSS_SELECTOR, "[data-product_id='182']")
    CHECKOUT_BTN = (By.CSS_SELECTOR, "[class='single_add_to_cart_button button alt']")
    MSG_ADDED_TOV = (By.XPATH, "//*[text()=' “HTML5 Forms” has been added to your basket.']")
    CHECKOUT_PAGE = (By.CSS_SELECTOR, "[class='wpmenucart-contents']")
    COUNT_TOV_IN_CHECKOUT = (By.XPATH, "//*[text()='1 item']")
