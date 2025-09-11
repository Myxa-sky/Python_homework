import pytest
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from pages.login_page import LoginPage
from pages.main_page import MainPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage
import time


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.get("https://www.saucedemo.com/")
    driver.maximize_window()
    yield driver
    # Сохраняем скриншот при падении теста (альтернативный способ)
    if hasattr(pytest, 'test_failed') and pytest.test_failed:
        driver.save_screenshot("error_screenshot.png")
    driver.quit()


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    # Хук для определения упавших тестов
    outcome = yield
    rep = outcome.get_result()
    if rep.when == "call" and rep.failed:
        pytest.test_failed = True


def test_complete_purchase(driver):
    print("\n=== Начало теста ===")
    pytest.test_failed = False  # Инициализируем флаг

    try:
        # 1. Авторизация
        print("Шаг 1: Авторизация")
        login_page = LoginPage(driver)
        login_page.enter_username("standard_user")
        login_page.enter_password("secret_sauce")
        login_page.click_login()

        assert "inventory" in driver.current_url, "Не удалось авторизоваться"
        print("Авторизация успешна")

        # 2. Добавление товаров в корзину
        print("Шаг 2: Добавление товаров")
        main_page = MainPage(driver)
        main_page.add_items_to_cart()
        main_page.go_to_cart()

        assert "cart" in driver.current_url, "Не удалось перейти в корзину"
        print("Товары добавлены, корзина открыта")

        # 3. Переход к оформлению заказа
        print("Шаг 3: Оформление заказа")
        cart_page = CartPage(driver)
        cart_page.click_checkout()

        print(f"Текущий URL: {driver.current_url}")
        time.sleep(1)  # Только для отладки

        assert "checkout-step-one" in driver.current_url, "Не удалось перейти к оформлению"
        print("Страница оформления загружена")

        # 4. Заполнение данных
        print("Шаг 4: Заполнение данных")
        checkout_page = CheckoutPage(driver)
        checkout_page.fill_checkout_info("John", "Doe", "12345")
        checkout_page.proceed_to_payment()

        assert "checkout-step-two" in driver.current_url, "Не удалось перейти к оплате"
        print("Данные заполнены, переход к оплате")

        # 5. Проверка итоговой суммы
        print("Шаг 5: Проверка суммы")
        total_text = checkout_page.get_total_amount()
        print(f"Итоговая сумма: {total_text}")

        assert "58.29" in total_text, f"Ожидалась сумма $58.29, но получено: {total_text}"
        print("=== Тест успешно завершен ===")

    except NoSuchElementException as e:
        pytest.test_failed = True
        print(f"ОШИБКА: Элемент не найден - {str(e)}")
        raise
    except AssertionError as e:
        pytest.test_failed = True
        print(f"ОШИБКА: Утверждение не выполнено - {str(e)}")
        raise
    except Exception as e:
        pytest.test_failed = True
        print(f"НЕОЖИДАННАЯ ОШИБКА: {str(e)}")
        raise
