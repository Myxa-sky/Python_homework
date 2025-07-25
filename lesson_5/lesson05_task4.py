from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.firefox import GeckoDriverManager


def main():
    # 1. Настройка драйвера (автоматическая установка)
    service = FirefoxService(GeckoDriverManager().install())

    # Опциональные настройки Firefox
    options = webdriver.FirefoxOptions()
    options.add_argument("--width=1280")
    options.add_argument("--height=720")

    # 2. Инициализация драйвера
    driver = webdriver.Firefox(service=service, options=options)

    try:
        # 3. Открытие страницы логина
        driver.get("http://the-internet.herokuapp.com/login")

        # 4. Ввод логина и пароля
        driver.find_element(By.ID, "username").send_keys("tomsmith")
        driver.find_element(By.ID, "password").send_keys("SuperSecretPassword!")

        # 5. Клик по кнопке Login
        driver.find_element(By.CSS_SELECTOR, "button.radius").click()

        # 6. Ожидание и получение сообщения
        flash = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.ID, "flash"))
        )
        success_text = flash.text.split("\n")[0]
        print(f"Успешная авторизация: {success_text}")

    except Exception as e:
        print(f"Ошибка: {str(e)}")
    finally:
        # 7. Закрытие браузера
        driver.quit()


if __name__ == "__main__":
    main()

