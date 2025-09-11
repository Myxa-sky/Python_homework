from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


class CalculatorPage:
    def __init__(self, driver):
        self.driver = driver
        self.delay_input = (By.CSS_SELECTOR, "#delay")
        self.result_screen = (By.CLASS_NAME, "screen")

        # Локаторы кнопок
        self.button_7 = (By.XPATH, "//span[text()='7']")
        self.button_8 = (By.XPATH, "//span[text()='8']")
        self.button_plus = (By.XPATH, "//span[text()='+']")
        self.button_equals = (By.XPATH, "//span[text()='=']")

    def open(self):
        self.driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")
        time.sleep(2)  # Простая пауза вместо ожидания элемента

    def set_delay(self, delay):
        delay_field = self.driver.find_element(*self.delay_input)
        delay_field.clear()
        delay_field.send_keys(str(delay))
        time.sleep(1)

    def click_7(self):
        self.driver.find_element(*self.button_7).click()
        time.sleep(0.3)

    def click_8(self):
        self.driver.find_element(*self.button_8).click()
        time.sleep(0.3)

    def click_plus(self):
        self.driver.find_element(*self.button_plus).click()
        time.sleep(0.3)

    def click_equals(self):
        self.driver.find_element(*self.button_equals).click()
        time.sleep(0.5)

    def get_result(self, timeout=50):
        # Простое ожидание без сложных условий
        time.sleep(timeout)
        return self.driver.find_element(*self.result_screen).text
