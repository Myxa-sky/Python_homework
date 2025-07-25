from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.common.by import By
from webdriver_manager.firefox import GeckoDriverManager


def main():
    # 1. Настройка драйвера Firefox
    service = FirefoxService(GeckoDriverManager().install())
    driver = webdriver.Firefox(service=service)

    try:
        # 2. Переход на страницу
        driver.get("http://the-internet.herokuapp.com/inputs")

        # 3. Находим поле ввода
        input_field = driver.find_element(By.TAG_NAME, "input")

        # 4. Вводим "Sky"
        input_field.send_keys("Sky")
        print("Введен текст 'Sky'")

        # 5. Очищаем поле
        input_field.clear()
        print("Поле очищено")

        # 6. Вводим "Pro"
        input_field.send_keys("Pro")
        print("Введен текст 'Pro'")

    except Exception as e:
        print(f"Ошибка при выполнении: {str(e)}")
    finally:
        # 7. Закрываем браузер
        driver.quit()
        print("Браузер закрыт")


if __name__ == "__main__":
    main()
