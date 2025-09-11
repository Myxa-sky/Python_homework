from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure
from allure import attachment_type


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

    @allure.step("Заполнение информации о доставке: {first_name} {last_name}, {postal_code}")
    def fill_checkout_info(self, first_name, last_name, postal_code):
        """Заполняет форму оформления заказа"""
        try:
            # Ждем появления формы
            WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located(self.first_name)
            )

            # Заполняем поля с прикреплением скриншотов
            self.driver.find_element(*self.first_name).send_keys(first_name)
            allure.attach(f"Заполнено First Name: {first_name}", "Данные формы", attachment_type.TEXT)

            self.driver.find_element(*self.last_name).send_keys(last_name)
            allure.attach(f"Заполнено Last Name: {last_name}", "Данные формы", attachment_type.TEXT)

            self.driver.find_element(*self.postal_code).send_keys(postal_code)
            allure.attach(f"Заполнено Postal Code: {postal_code}", "Данные формы", attachment_type.TEXT)

            # Скриншот заполненной формы
            allure.attach(
                self.driver.get_screenshot_as_png(),
                name="checkout_form_filled",
                attachment_type=attachment_type.PNG
            )

        except Exception as e:
            print(f"Ошибка при заполнении формы: {e}")
            # Скриншот при ошибке
            allure.attach(
                self.driver.get_screenshot_as_png(),
                name="checkout_form_error",
                attachment_type=attachment_type.PNG
            )
            raise

    @allure.step("Нажатие кнопки Continue")
    def proceed_to_payment(self):
        """Нажимает кнопку Continue для перехода к оплате"""
        try:
            WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(self.continue_button)
            ).click()

            # Скриншот после нажатия
            allure.attach(
                self.driver.get_screenshot_as_png(),
                name="after_continue_click",
                attachment_type=attachment_type.PNG
            )

        except Exception as e:
            print(f"Ошибка при нажатии кнопки Continue: {e}")
            allure.attach(
                self.driver.get_screenshot_as_png(),
                name="continue_button_error",
                attachment_type=attachment_type.PNG
            )
            raise

    @allure.step("Получение итоговой суммы")
    def get_total_amount(self):
        """Возвращает итоговую сумму"""
        return WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.total_amount)
        ).text

    @allure.step("Проверка сообщения об ошибке")
    def get_error_message(self):
        """Возвращает сообщение об ошибке, если есть"""
        try:
            return self.driver.find_element(*self.error_message).text
        except:
            return "Ошибок нет"
