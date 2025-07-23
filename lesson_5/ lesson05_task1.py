from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

# Укажите полный путь к chromedriver.exe
service = Service(executable_path=r'C:\Users\user\Desktop\Python_hw\Python_homework\lesson_5\chromedriver.exe')
driver = webdriver.Chrome(service=service)

try:
    driver.get("http://uitestingplayground.com/classattr")
    blue_button = driver.find_element(By.XPATH, "//button[contains(@class, 'btn-primary')]")
    blue_button.click()
    print("Успешный клик!")

    # Обработка алерта (если появится)
    alert = driver.switch_to.alert
    alert.accept()

finally:
    driver.quit()
