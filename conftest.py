import pytest
import allure
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from constants import WINDOW_SIZE


def pytest_addoption(parser):
    parser.addoption('--language', action='store', default=None, help="Choose language")


@pytest.fixture(scope="function")
def browser(request):
    l_language = request.config.getoption('language')
    l_options = Options()
    l_options.add_experimental_option('prefs', {'intl.accept_languages': l_language})
    browser = webdriver.Chrome(r'C:\\Selenium\\chromedriver.exe', options=l_options)
    browser.set_window_size(*WINDOW_SIZE)
    with allure.step(f"Browser:{browser} Windows size:{WINDOW_SIZE} Language:{l_language}"):
        pass
    yield browser
    browser.quit()
