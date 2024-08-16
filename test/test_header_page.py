import allure
from utils.urls import Urls
from locators.main_page_locators import MainPageLocators
from pages.main_page import YaScooterMainPage


class TestYaScooterMainPage:

    @allure.title('Проверка перехода на главную страницу')
    @allure.description('Клик на лого Самоката ведёт на главную страницу')
    def test_click_samokat_logo(self, driver):
        ya_scooter_main_page = YaScooterMainPage(driver)
        ya_scooter_main_page.go_to_site()
        ya_scooter_main_page.click_accept_cookies()
        ya_scooter_main_page.click_order_button(MainPageLocators.ORDER_BUTTON_IN_HEADER)
        ya_scooter_main_page.click_samokat_logo()
        assert ya_scooter_main_page.current_url() == Urls.MAIN_URL

    @allure.title('Проверка перехода на Дзен')
    @allure.description('Клик на лого Яндекса ведёт переход на Дзен')
    def test_click_yandex_logo(self, driver):
        ya_scooter_main_page = YaScooterMainPage(driver)
        ya_scooter_main_page.go_to_site()
        ya_scooter_main_page.click_accept_cookies()
        ya_scooter_main_page.click_yandex_logo()
        ya_scooter_main_page.switch_window(1)
        ya_scooter_main_page.wait_url_until_not_about_blank()
        current_url = ya_scooter_main_page.current_url()
        assert Urls.DZEN_PAGE in current_url