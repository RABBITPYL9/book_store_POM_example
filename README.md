


Запуск тестов выполняется в командной строке:
```
pytest -v --tb=line --language=en --alluredir=allure_report -m need_review 
pytest -v --tb=line --language=en --alluredir=allure_report -m need_review_custom_scenarios
```
Для генерации отчета Allure выполнить команду:
```
allure serve /path_to/allure_report/
```

## Built With
* [Selenium WebDriver](https://www.selenium.dev/documentation/en/webdriver/) -  The Selenium Browser Automation Project
* [Allure framework](https://github.com/allure-framework) - A flexible lightweight multi-language test report tool
* [Pytest](https://docs.pytest.org/en/stable/) - The pytest framework makes it easy to write small tests, yet scales to support complex functional testing for applications and libraries
