import pytest
from selenium import webdriver
from calculator_page import CalculatorPage


@pytest.fixture
def browser():
    driver = webdriver.Chrome()
    driver.implicitly_wait(5)
    yield driver
    driver.quit()


def test_calculator_with_delay(browser):
    calculator = CalculatorPage(browser)

    # 1. Открываем страницу
    calculator.open()

    # 2. Устанавливаем задержку
    calculator.set_delay(45)

    # 3. Вводим выражение 7 + 8
    calculator.click_7()
    calculator.click_plus()
    calculator.click_8()

    # 4. Нажимаем равно
    calculator.click_equals()

    # 5. Проверяем результат
    result = calculator.get_result()
    assert result == "15", f"Ожидался результат 15, получен {result}"
