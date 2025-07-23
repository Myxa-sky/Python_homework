from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

# Укажите полный путь к драйверу через Service
service = Service(executable_path=r'C:\Users\user\Desktop\Python_hw\Python_homework\lesson_5\chromedriver.exe')
driver = webdriver.Chrome(service=service)

try:
    driver.get("http://uitestingplayground.com/dynamicid")

    # Находим кнопку по классу (игнорируя динамический ID)
    button = driver.find_element(By.CSS_SELECTOR, "button.btn-primary")
    button.click()
    print("Успешный клик по кнопке с динамическим ID!")

finally:
    driver.quit()
