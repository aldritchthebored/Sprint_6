import allure
from selenium.webdriver import Keys
from pages.base_page import BasePage
from locators.order_page_locators import OrderPageLocators
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class YaScooterOrderPage(BasePage):
    @allure.step('Заполнить поле "Имя"')
    def set_name(self, name):
        return self.send_keys(OrderPageLocators.NAME_INPUT, name)

    @allure.step('Заполнить поле "Фамилия"')
    def set_surname(self, surname):
        return self.send_keys(OrderPageLocators.SURNAME_INPUT, surname)

    @allure.step('Заполнить поле "Адрес"')
    def set_address(self, address):
        return self.send_keys(OrderPageLocators.ADDRESS_INPUT, address)

    @allure.step('Нажать на поле "Станция метро"')
    def click_metro_button(self):
        return self.find_element(OrderPageLocators.METRO_STATION_BUTTON).click()

    @allure.step('Выбрать станцию')
    def select_metro_station(self, metro):
        return self.find_element(metro).click()

    @allure.step('Заполнить поле "Телефон"')
    def set_phone(self, phone):
        return self.send_keys(OrderPageLocators.PHONE_INPUT, phone)

    @allure.step('Нажать на кнопку "Заказать"')
    def click_order_button(self):
        return self.find_element(OrderPageLocators.NEXT_BUTTON).click()

    @allure.step('Ввод даты')
    def set_date(self, date):
        self.send_keys(OrderPageLocators.DATE_DELIVER_BUTTON, date)
        return self.send_keys(OrderPageLocators.DATE_DELIVER_BUTTON, Keys.ENTER)

    @allure.step('Выбор периода аренды')
    def set_rental_duration(self, rental_duration):
        self.find_element(OrderPageLocators.RENT_DATE_BUTTON).click()
        return self.find_element(rental_duration).click()

    @allure.step('Выбор цвета')
    def choose_color(self, color):
        return self.find_element(color).click()

    @allure.step('Комментарий для курьера')
    def set_comment(self, commentary_text):
        return self.send_keys(OrderPageLocators.COMMENT_INPUT, commentary_text)

    @allure.step('Нажать "Заказать"')
    def click_order_scooter(self):
        return self.find_element(OrderPageLocators.ORDER_BUTTON).click()

    @allure.step('Подтвердить заказ')
    def click_accept_order(self):
        return self.find_element(OrderPageLocators.CONFIRM_ORDER_BUTTON).click()

    @allure.step('Проверка появления окна создания заказа с кнопкой "Посмотреть статус"')
    def check_success_window(self):
        return self.find_element(OrderPageLocators.CHECK_STATUS_BUTTON).text
        
    @allure.step('Заполнить данные "Для кого самокат"')
    def fill_user_data(self, name, surname, address, phone, metro):
        self.set_name(name)
        self.set_surname(surname)
        self.set_address(address)
        self.click_metro_button()
        self.select_metro_station(metro)
        self.set_phone(phone)

    @allure.step('Заполнить данные на этапе "Про аренду"')
    def fill_rent_data(self, date, rental_duration, color, commentary):
        self.set_date(date)
        self.set_rental_duration(rental_duration)
        self.choose_color(color)
        self.set_comment(commentary)


    
    