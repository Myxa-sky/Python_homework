from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest


@pytest.fixture
def browser():
    driver = webdriver.Firefox()
    yield driver
    driver.quit()


def test_shopping(browser):
    # 1. Открыть сайт магазина
    browser.get("https://www.saucedemo.com/")

    # 2. Авторизоваться
    browser.find_element(By.ID, "user-name").send_keys("standard_user")
    browser.find_element(By.ID, "password").send_keys("secret_sauce")
    browser.find_element(By.ID, "login-button").click()

    # 3. Добавить товары в корзину
    items = [
        "Sauce Labs Backpack",
        "Sauce Labs Bolt T-Shirt",
        "Sauce Labs Onesie"
    ]

    for item in items:
        browser.find_element(By.XPATH, f"//div[text()='{item}']/ancestor::div[@class='inventory_item']//button").click()

    # 4. Перейти в корзину
    browser.find_element(By.CLASS_NAME, "shopping_cart_link").click()

    # 5. Нажать Checkout
    browser.find_element(By.ID, "checkout").click()

    # 6. Заполнить форму
    browser.find_element(By.ID, "first-name").send_keys("Иван")
    browser.find_element(By.ID, "last-name").send_keys("Петров")
    browser.find_element(By.ID, "postal-code").send_keys("123456")

    # 7. Нажать Continue
    browser.find_element(By.ID, "continue").click()

    # 8. Прочитать итоговую стоимость
    total_element = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "summary_total_label"))
    )
    total = total_element.text

    # 9. Закрыть браузер (делается в фикстуре)

    # 10. Проверить итоговую сумму
    assert total == "Total: $58.29"
