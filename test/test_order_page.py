import pytest
import allure
from utils.urls import Urls
from utils.test_data import YaScooterOrderData
from locators.main_page_locators import MainPageLocators
from locators.order_page_locators import OrderPageLocators
from pages.main_page import YaScooterMainPage
from pages.order_page import YaScooterOrderPage


class TestYaScooterOrderPage:

    @pytest.mark.parametrize(
        'order_button, user_data, metro_button, days_duration, colour_button',
        [
            [MainPageLocators.ORDER_BUTTON_IN_HEADER, YaScooterOrderData.order_1, OrderPageLocators.PEROVO_STATION_BUTTON,
            OrderPageLocators.ONE_DAY_RENT, OrderPageLocators.BLACK_COLOR],
            [MainPageLocators.ORDER_BUTTON, YaScooterOrderData.order_2, OrderPageLocators.DUBROVKA_STATION_BUTTON,
            OrderPageLocators.TWO_DAY_RENT, OrderPageLocators.GREY_COLOR]
        ]
    )
    @allure.title('Тест заказа доставки самоката')
    @allure.description(
        'Кликнуть на кнопку "Заказать", заполнить форму валидными данными и появляется окно "Посмотреть статус" '
    )
    def test_scooter_orders(self, driver, order_button, user_data, metro_button, days_duration, colour_button):
        main_page = YaScooterMainPage(driver)
        main_page.go_to_site()
        main_page.click_accept_cookies()
        main_page.click_order_button(order_button)
        order_page = YaScooterOrderPage(driver)
        order_page.fill_user_data(user_data[0], user_data[1], user_data[2], user_data[3], metro_button)
        order_page.click_order_button()
        order_page.fill_rent_data(user_data[4], days_duration, colour_button, user_data[5])
        order_page.click_order_scooter()
        order_page.click_accept_order()
        window_sucess = order_page.check_success_window()
        assert window_sucess == 'Посмотреть статус', 'Окно создания заказа с кнопкой "Посмотреть статус" не появилось'

