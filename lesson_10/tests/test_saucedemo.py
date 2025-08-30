import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from webdriver_manager.firefox import GeckoDriverManager  # ← ДЛЯ FIREFOX
from webdriver_manager.chrome import ChromeDriverManager
from pages.login_page import LoginPage
from pages.main_page import MainPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage
import allure
from allure import attachment_type


@pytest.fixture
def driver():
    """Фикстура для Firefox браузера"""
    # Используем Firefox вместо Chrome!
    driver = webdriver.Firefox()

    driver.get("https://www.saucedemo.com/")
    driver.maximize_window()

    yield driver
    driver.quit()


@allure.epic("SauceDemo магазин")
@allure.feature("Полный цикл покупки")
@allure.severity(allure.severity_level.CRITICAL)
@allure.title("Полное оформление заказа с проверкой суммы")
def test_complete_purchase(driver):
    try:
        with allure.step("Авторизация пользователя в Firefox"):
            login_page = LoginPage(driver)
            login_page.enter_username("standard_user")
            login_page.enter_password("secret_sauce")
            login_page.click_login()

            WebDriverWait(driver, 10).until(EC.url_contains("inventory"))
            allure.attach(driver.get_screenshot_as_png(), "after_login", attachment_type.PNG)
            print("✅ Успешная авторизация в Firefox")

        with allure.step("Добавление товаров в корзину"):
            main_page = MainPage(driver)
            main_page.add_items_to_cart()
            WebDriverWait(driver, 5).until(
                EC.presence_of_element_located((By.CLASS_NAME, "shopping_cart_badge"))
            )
            allure.attach(driver.get_screenshot_as_png(), "items_added", attachment_type.PNG)

        with allure.step("Переход в корзину"):
            main_page.go_to_cart()
            WebDriverWait(driver, 10).until(EC.url_contains("cart"))
            allure.attach(driver.get_screenshot_as_png(), "cart_page", attachment_type.PNG)

        with allure.step("Начало оформления заказа"):
            cart_page = CartPage(driver)
            cart_page.click_checkout()
            WebDriverWait(driver, 10).until(EC.url_contains("checkout-step-one"))
            allure.attach(driver.get_screenshot_as_png(), "checkout_step1", attachment_type.PNG)

        with allure.step("Заполнение данных доставки"):
            checkout_page = CheckoutPage(driver)
            checkout_page.fill_checkout_info("John", "Doe", "12345")
            checkout_page.proceed_to_payment()
            WebDriverWait(driver, 10).until(EC.url_contains("checkout-step-two"))
            allure.attach(driver.get_screenshot_as_png(), "checkout_step2", attachment_type.PNG)

        with allure.step("Проверка итоговой суммы"):
            total_text = checkout_page.get_total_amount()
            assert "58.29" in total_text, f"Ожидалась сумма $58.29, но получено: {total_text}"
            allure.attach(f"Итоговая сумма: {total_text}", "Total Amount", attachment_type.TEXT)
            print("✅ Тест успешно завершен в Firefox!")

    except Exception as e:
        allure.attach(driver.get_screenshot_as_png(), "final_error_state", attachment_type.PNG)
        print(f"❌ Ошибка: {e}")
        raise
