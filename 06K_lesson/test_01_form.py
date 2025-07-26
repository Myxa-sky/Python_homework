import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture
def driver():
    # Инициализация Edge с опциями
    options = webdriver.EdgeOptions()
    options.add_argument("--start-maximized")
    driver = webdriver.Edge(options=options)
    yield driver
    # Закрытие браузера
    driver.quit()


def test_form_validation(driver):
    """Тест проверяет валидацию формы с подсветкой полей"""
    # 1. Открытие страницы
    driver.get("https://bonigarcia.dev/selenium-webdriver-java/data-types.html")

    # 2. Данные для заполнения
    test_data = {
        "first-name": "Иван",
        "last-name": "Petrov",
        "address": "Ленина, 55-3",
        "e-mail": "test@skypro.com",
        "phone": "+79858999887",  # 11 цифр
        # zip-code оставляем пустым
        "city": "Москва",
        "country": "Россия",
        "job-position": "QA",
        "company": "SkyPro"
    }

    # 3. Заполнение формы
    for field, value in test_data.items():
        element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.NAME, field)))
        element.clear()
        element.send_keys(value)

    # 4. Отправка формы
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type='submit']"))).click()

    # 5. Проверка результатов
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, ".alert")))

    # Проверка zip-code
    zip_code = driver.find_element(By.ID, "zip-code")
    assert all([
        "alert-danger" in zip_code.get_attribute("class"),
        zip_code.text == "N/A"
    ]), "Zip code должен быть подсвечен красным с текстом N/A"

    # Проверка остальных полей
    for field, expected_value in test_data.items():
        element = driver.find_element(By.ID, field)
        assert all([
            "alert-success" in element.get_attribute("class"),
            element.text == expected_value
        ]), f"Поле {field} должно быть валидным со значением {expected_value}"
