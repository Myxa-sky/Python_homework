import pytest
from selenium import webdriver
from selenium.webdriver.remote.webdriver import WebDriver
from calculator_page import CalculatorPage
import allure


@pytest.fixture
def browser() -> WebDriver:
    """
    Фикстура для инициализации и закрытия браузера.

    :return: WebDriver instance
    """
    driver = webdriver.Chrome()
    driver.implicitly_wait(5)
    yield driver
    driver.quit()


@allure.epic("Калькулятор с задержкой")
@allure.feature("Базовые операции")
@allure.severity(allure.severity_level.CRITICAL)
class TestCalculator:
    """Тесты для калькулятора с задержкой выполнения."""

    @allure.id("CALC-001")
    @allure.story("Сложение чисел")
    @allure.title("Проверка сложения 7 + 8 с задержкой 45 секунд")
    @allure.description("""
    Тест проверяет корректность работы калькулятора с установленной задержкой.
    Шаги:
    1. Открыть страницу калькулятора
    2. Установить задержку 45 секунд
    3. Ввести выражение 7 + 8
    4. Нажать кнопку равно
    5. Дождаться результата и проверить его
    Ожидаемый результат: 15
    """)
    def test_calculator_with_delay(self, browser: WebDriver) -> None:
        calculator = CalculatorPage(browser)

        with allure.step("Открытие страницы калькулятора"):
            calculator.open()

        with allure.step("Установка задержки вычислений"):
            calculator.set_delay(45)

        with allure.step("Ввод выражения 7 + 8"):
            calculator.click_7()
            calculator.click_plus()
            calculator.click_8()

        with allure.step("Запуск вычисления"):
            calculator.click_equals()

        with allure.step("Проверка результата"):
            result = calculator.get_result()
            assert result == "15", f"Ожидался результат 15, получен {result}"
            allure.attach(
                f"Результат вычислений: {result}",
                name="calculation_result",
                attachment_type=allure.attachment_type.TEXT
            )
