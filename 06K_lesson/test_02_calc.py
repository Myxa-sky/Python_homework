from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest


@pytest.fixture
def browser():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()


def test_calculator(browser):
    # 1. Открыть страницу
    browser.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")

    # 2. Ввести задержку 45
    browser.find_element(By.CSS_SELECTOR, "#delay").clear()
    browser.find_element(By.CSS_SELECTOR, "#delay").send_keys("45")

    # 3. Нажать кнопки 7 + 8 =
    browser.find_element(By.XPATH, "//span[text()='7']").click()
    browser.find_element(By.XPATH, "//span[text()='+']").click()
    browser.find_element(By.XPATH, "//span[text()='8']").click()
    browser.find_element(By.XPATH, "//span[text()='=']").click()

    # 4. Проверить результат через 45 секунд
    result = WebDriverWait(browser, 46).until(
        EC.text_to_be_present_in_element((By.CSS_SELECTOR, ".screen"), "15")
    )
    assert result
