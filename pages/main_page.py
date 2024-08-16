import allure
from pages.base_page import BasePage
from locators.main_page_locators import MainPageLocators
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class YaScooterMainPage(BasePage):
    @allure.step('Нажать на кнопку заказа')
    def click_order_button(self, order_button):
        self.find_element(order_button).click()

    @allure.step('Нажать на вопросы FAQ')
    def click_faq_question(self, question):
        self.find_element(question).click()

    @allure.step('Получить текст ответа')
    def get_answer_text(self, answer):
        actually_text = self.find_element(answer).text
        return actually_text

    @allure.step('Переключиться на вкладку браузера')
    def switch_window(self, window_number: int = 1):
        self.driver.switch_to.window(self.driver.window_handles[window_number])

    def wait_url_until_not_about_blank(self, time=10):
        WebDriverWait(self.driver, time).until_not(EC.url_to_be('about:blank'))

    @allure.step('Перейти на страницу яндекса')
    def click_yandex_logo(self):
        self.find_element(MainPageLocators.YANDEX_LOGO).click()
    
    @allure.step('Перейти на страницу самоката')
    def click_samokat_logo(self):
        self.find_element(MainPageLocators.SAMOKAT_LOGO).click()

    @allure.step('Принять куки')
    def click_accept_cookies(self):
        self.find_element(MainPageLocators.ACCEPT_COOKIE_BUTTON).click()
