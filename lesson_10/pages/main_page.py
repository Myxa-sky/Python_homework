from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure


class MainPage:
    def __init__(self, driver):
        self.driver = driver
        self.add_backpack = (By.ID, "add-to-cart-sauce-labs-backpack")
        self.add_bolt_tshirt = (By.ID, "add-to-cart-sauce-labs-bolt-t-shirt")
        self.add_onesie = (By.ID, "add-to-cart-sauce-labs-onesie")
        self.cart_button = (By.CLASS_NAME, "shopping_cart_link")

    @allure.step("Добавление товаров в корзину")
    def add_items_to_cart(self) -> None:
        """Добавляет три товара в корзину."""
        self.driver.find_element(*self.add_backpack).click()
        self.driver.find_element(*self.add_bolt_tshirt).click()
        self.driver.find_element(*self.add_onesie).click()

    @allure.step("Переход в корзину")
    def go_to_cart(self) -> None:
        """Переходит в корзину с ожиданием загрузки."""
        # Нажимаем на кнопку корзины
        cart_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.cart_button)
        )
        cart_button.click()

        # Ждем загрузки страницы корзины
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "cart_list"))
        )
