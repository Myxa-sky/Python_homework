from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get("https://bonigarcia.dev/selenium-webdriver-java/loading-images.html")

# Ожидаем загрузки всех изображений (ждем, пока последнее изображение не загрузится)
WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.CSS_SELECTOR, "#image-container img:nth-child(4)")))

# Получаем src третьего изображения (индексация с 0)
third_image = driver.find_element(By.CSS_SELECTOR, "#image-container img:nth-child(3)")
print(third_image.get_attribute("src"))

driver.quit()
