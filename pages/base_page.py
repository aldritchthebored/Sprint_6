import allure
from utils.urls import Urls
from locators.main_page_locators import MainPageLocators
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def find_element(self, locator, time=10):
        return WebDriverWait(self.driver, time).until(EC.presence_of_element_located(locator))

    def send_keys(self, locator, value):
        self.driver.find_element(*locator).send_keys(value)

    @allure.step('Перейти по адресу')
    def go_to_site(self):
        self.driver.get(Urls.MAIN_URL)

    @allure.step('Получить текущий URL')
    def current_url(self):
        return self.driver.current_url
