from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
import allure


class LoginPage:
    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.username_field = (By.ID, "user-name")
        self.password_field = (By.ID, "password")
        self.login_button = (By.ID, "login-button")

    @allure.step("Ввод username: {username}")
    def enter_username(self, username: str) -> None:
        self.driver.find_element(*self.username_field).send_keys(username)

    @allure.step("Ввод пароля")
    def enter_password(self, password: str) -> None:
        self.driver.find_element(*self.password_field).send_keys(password)

    @allure.step("Нажатие кнопки Login")
    def click_login(self) -> None:
        self.driver.find_element(*self.login_button).click()
