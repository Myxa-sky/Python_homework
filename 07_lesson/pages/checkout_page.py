from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CheckoutPage:
    def __init__(self, driver):
        self.driver = driver
        # Локаторы для формы оформления заказа
        self.first_name = (By.ID, "first-name")
        self.last_name = (By.ID, "last-name")
        self.postal_code = (By.ID, "postal-code")
        self.continue_button = (By.ID, "continue")
        self.total_amount = (By.CSS_SELECTOR, ".summary_total_label")
        self.error_message = (By.CSS_SELECTOR, "[data-test='error']")

    def fill_checkout_info(self, first_name, last_name, postal_code):
        """Заполняет форму оформления заказа"""
        try:
            WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located(self.first_name)
            ).send_keys(first_name)

            self.driver.find_element(*self.last_name).send_keys(last_name)
            self.driver.find_element(*self.postal_code).send_keys(postal_code)
        except Exception as e:
            print(f"Ошибка при заполнении формы: {e}")
            raise

    def proceed_to_payment(self):
        """Нажимает кнопку Continue для перехода к оплате"""
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.continue_button)
        ).click()

    def get_total_amount(self):
        """Возвращает итоговую сумму"""
        return WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.total_amount)
        ).text

    def get_error_message(self):
        """Возвращает сообщение об ошибке, если есть"""
        return self.driver.find_element(*self.error_message).text
