from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class CartPage:
    def __init__(self, driver):
        self.driver = driver
        # Локаторы элементов страницы корзины
        self.checkout_button = (By.ID, "checkout")
        self.cart_items = (By.CLASS_NAME, "cart_item")
        self.continue_shopping_btn = (By.ID, "continue-shopping")
        self.remove_buttons = (By.XPATH, "//button[contains(@class, 'cart_button')]")

    def click_checkout(self):
        """Нажимает кнопку Checkout с явным ожиданием"""
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.checkout_button)
        ).click()

    def get_cart_items_count(self):
        """Возвращает количество товаров в корзине"""
        return len(self.driver.find_elements(*self.cart_items))

    def remove_item(self, index=0):
        """Удаляет товар из корзины по индексу"""
        remove_buttons = self.driver.find_elements(*self.remove_buttons)
        if index < len(remove_buttons):
            remove_buttons[index].click()

    def continue_shopping(self):
        """Нажимает кнопку Continue Shopping"""
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.continue_shopping_btn)
        ).click()
