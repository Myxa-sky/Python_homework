from selenium import webdriver
from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest
import os


@pytest.fixture
def browser():
    driver_path = os.path.join(os.getcwd(), "msedgedriver.exe")
    service = EdgeService(executable_path=driver_path)
    options = webdriver.EdgeOptions()
    options.add_argument("--start-maximized")
    driver = webdriver.Edge(service=service, options=options)
    yield driver
    driver.quit()


def test_form_submission(browser):
    try:
        # 1. Открыть страницу
        browser.get("https://bonigarcia.dev/selenium-webdriver-java/data-types.html")

        # 2. Дождаться загрузки формы
        WebDriverWait(browser, 20).until(
            EC.presence_of_element_located((By.TAG_NAME, "form"))
        )

        # 3. Заполнить форму
        fields = {
            "first-name": "Иван",
            "last-name": "Петров",
            "address": "Ленина, 55-3",
            "e-mail": "test@skypro.com",
            "phone": "+7985899988787",
            "city": "Москва",
            "country": "Россия",
            "job-position": "QA",
            "company": "SkyPro"
        }

        for field_name, value in fields.items():
            element = WebDriverWait(browser, 10).until(
                EC.presence_of_element_located((By.NAME, field_name))
            )
            element.clear()
            element.send_keys(value)

        # 4. Оставить поле Zip code пустым

        # 5. Нажать кнопку Submit
        submit = WebDriverWait(browser, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//button[@type='submit']"))
        )
        submit.click()

        # 6. Проверить, что произошел переход на новую страницу
        WebDriverWait(browser, 10).until(
            EC.url_contains("data-types-submitted.html")
        )

        # 7. Проверить, что в URL присутствуют переданные параметры
        current_url = browser.current_url
        assert "first-name=%D0%98%D0%B2%D0%B0%D0%BD" in current_url
        assert "last-name=%D0%9F%D0%B5%D1%82%D1%80%D0%BE%D0%B2" in current_url
        assert "zip-code=" in current_url  # Пустое поле

    except Exception as e:
        browser.save_screenshot("error.png")
        print("Current URL:", browser.current_url)
        print("Page title:", browser.title)
        raise e
