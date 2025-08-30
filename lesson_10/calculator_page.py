from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webdriver import WebDriver
import time
import allure
from allure import attachment_type


class CalculatorPage:
    """Page Object класс для калькулятора с задержкой."""

    def __init__(self, driver: WebDriver) -> None:
        """
        Инициализирует страницу калькулятора.

        :param driver: WebDriver instance
        """
        self.driver = driver
        self.delay_input = (By.CSS_SELECTOR, "#delay")
        self.result_screen = (By.CLASS_NAME, "screen")

        # Локаторы кнопок
        self.button_7 = (By.XPATH, "//span[text()='7']")
        self.button_8 = (By.XPATH, "//span[text()='8']")
        self.button_plus = (By.XPATH, "//span[text()='+']")
        self.button_equals = (By.XPATH, "//span[text()='=']")

    @allure.step("Открыть страницу калькулятора")
    def open(self) -> None:
        """
        Открывает страницу калькулятора.

        Переходит по URL и ждет загрузки страницы.
        """
        self.driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")
        time.sleep(2)
        allure.attach(
            self.driver.get_screenshot_as_png(),
            name="calculator_page_loaded",
            attachment_type=attachment_type.PNG
        )

    @allure.step("Установить задержку вычислений: {delay} секунд")
    def set_delay(self, delay: int) -> None:
        """
        Устанавливает время задержки вычислений.

        :param delay: Время задержки в секундах
        """
        delay_field = self.driver.find_element(*self.delay_input)
        delay_field.clear()
        delay_field.send_keys(str(delay))
        time.sleep(1)

    @allure.step("Нажать кнопку '7'")
    def click_7(self) -> None:
        """Нажимает кнопку с цифрой 7."""
        self.driver.find_element(*self.button_7).click()
        time.sleep(0.3)

    @allure.step("Нажать кнопку '8'")
    def click_8(self) -> None:
        """Нажимает кнопку с цифрой 8."""
        self.driver.find_element(*self.button_8).click()
        time.sleep(0.3)

    @allure.step("Нажать кнопку '+'")
    def click_plus(self) -> None:
        """Нажимает кнопку сложения."""
        self.driver.find_element(*self.button_plus).click()
        time.sleep(0.3)

    @allure.step("Нажать кнопку '='")
    def click_equals(self) -> None:
        """Нажимает кнопку вычисления результата."""
        self.driver.find_element(*self.button_equals).click()
        time.sleep(0.5)

    @allure.step("Получить результат вычислений")
    def get_result(self, timeout: int = 50) -> str:
        """
        Ожидает и возвращает результат вычислений.

        :param timeout: Максимальное время ожидания в секундах
        :return: Текст результата вычислений
        """
        time.sleep(timeout)
        result = self.driver.find_element(*self.result_screen).text

        # Делаем скриншот с результатом
        allure.attach(
            self.driver.get_screenshot_as_png(),
            name=f"result_{result}",
            attachment_type=attachment_type.PNG
        )

        return result
