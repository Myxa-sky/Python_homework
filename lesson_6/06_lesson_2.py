from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get("http://uitestingplayground.com/textinput")

# Вводим текст в поле
input_field = driver.find_element(By.CSS_SELECTOR, "#newButtonName")
input_field.send_keys("SkyPro")

# Нажимаем на синюю кнопку
blue_button = driver.find_element(By.CSS_SELECTOR, "#updatingButton")
blue_button.click()

# Получаем обновленный текст кнопки
button_text = WebDriverWait(driver, 10).until(
    EC.text_to_be_present_in_element((By.CSS_SELECTOR, "#updatingButton"), "SkyPro"))
updated_button = driver.find_element(By.CSS_SELECTOR, "#updatingButton")
print(updated_button.text)

driver.quit()
