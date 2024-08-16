from selenium.webdriver.common.by import By


class MainPageLocators:
    ACCEPT_COOKIE_BUTTON = (By.XPATH, ('//button[text()="да все привыкли"]'))  
    ORDER_BUTTON_IN_HEADER = (By.CLASS_NAME, 'Button_Button__ra12g')
    ORDER_BUTTON = (By.XPATH, '//*[contains(@class,"FinishButton")]//button[text()="Заказать"]')
    YANDEX_LOGO = (By.XPATH, '//img[@alt="Yandex"]/parent::a')
    SAMOKAT_LOGO = (By.XPATH, '//img[@alt="Scooter"]/parent::a')
    
    FAQ_Q_1 = (By.ID, 'accordion__heading-0')
    FAQ_A_1 = (By.XPATH, '//div[@id="accordion__panel-0"]/p')
    FAQ_Q_2 = (By.ID, 'accordion__heading-1')
    FAQ_A_2 = (By.XPATH, '//div[@id="accordion__panel-1"]/p')
    FAQ_Q_3 = (By.ID, 'accordion__heading-2')
    FAQ_A_3 = (By.XPATH, '//div[@id="accordion__panel-2"]/p')
    FAQ_Q_4 = (By.ID, 'accordion__heading-3')
    FAQ_A_4 = (By.XPATH, '//div[@id="accordion__panel-3"]/p')
    FAQ_Q_5 = (By.ID, 'accordion__heading-4')
    FAQ_A_5 = (By.XPATH, '//div[@id="accordion__panel-4"]/p')
    FAQ_Q_6 = (By.ID, 'accordion__heading-5')
    FAQ_A_6 = (By.XPATH, '//div[@id="accordion__panel-5"]/p')
    FAQ_Q_7 = (By.ID, 'accordion__heading-6')
    FAQ_A_7 = (By.XPATH, '//div[@id="accordion__panel-6"]/p')
    FAQ_Q_8 = (By.ID, 'accordion__heading-7')
    FAQ_A_8 = (By.XPATH, '//div[@id="accordion__panel-7"]/p')
