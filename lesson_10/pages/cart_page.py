from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure
from allure import attachment_type


class CartPage:
    def __init__(self, driver):
        self.driver = driver
        self.checkout_button = (By.ID, "checkout")
        self.cart_items = (By.CLASS_NAME, "cart_item")
        self.continue_shopping_btn = (By.ID, "continue-shopping")
        self.remove_buttons = (By.XPATH, "//button[contains(@class, 'cart_button')]")

    @allure.step("Нажатие кнопки Checkout")
    def click_checkout(self) -> None:
        """Нажимает кнопку Checkout"""
        checkout_btn = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.checkout_button)
        )
        checkout_btn.click()

    # Остальные методы остаются без изменений
    @allure.step("Получение количества товаров в корзине")
    def get_cart_items_count(self) -> int:
        return len(self.driver.find_elements(*self.cart_items))

    @allure.step("Удаление товара из корзины по индексу {index}")
    def remove_item(self, index: int = 0) -> None:
        remove_buttons = self.driver.find_elements(*self.remove_buttons)
        if index < len(remove_buttons):
            remove_buttons[index].click()

    @allure.step("Нажатие кнопки Continue Shopping")
    def continue_shopping(self) -> None:
        continue_btn = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.continue_shopping_btn)
        )
        continue_btn.click()
