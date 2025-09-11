import allure
import pytest
from selenium import webdriver


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """
    Хук для создания скриншотов при падении тестов.
    """
    outcome = yield
    result = outcome.get_result()

    if result.when == "call" and result.failed:
        browser = item.funcargs.get('browser')
        if browser is not None:
            allure.attach(
                browser.get_screenshot_as_png(),
                name="screenshot_on_failure",
                attachment_type=allure.attachment_type.PNG
            )
