from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get("http://uitestingplayground.com/ajax")

# Нажимаем на кнопку (AJAX запрос может быть медленным)
ajax_button = driver.find_element(By.ID, "ajaxButton")
ajax_button.click()

# Увеличиваем время ожидания и используем правильный локатор
success_message = WebDriverWait(driver, 20).until(
    EC.presence_of_element_located((By.CSS_SELECTOR, "p.bg-success"))
)

print(success_message.text)  # Должно вывести: "Data loaded with AJAX get request."

driver.quit()
