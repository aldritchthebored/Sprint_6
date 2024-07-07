from selenium.webdriver.common.by import By


class OrderPageLocators:
    NAME_INPUT = (By.XPATH, '//input[@placeholder="* Имя"]')
    SURNAME_INPUT = (By.XPATH, '//input[@placeholder="* Фамилия"]')
    ADDRESS_INPUT = (By.XPATH, '//input[@placeholder="* Адрес: куда привезти заказ"]')
    PHONE_INPUT = (By.XPATH, '//input[@placeholder="* Телефон: на него позвонит курьер"]')
    METRO_STATION_BUTTON = (By.XPATH, '//input[@placeholder="* Станция метро"]')
    PEROVO_STATION_BUTTON = (By.XPATH, '//div[text()="Перово"]')
    DUBROVKA_STATION_BUTTON = (By.XPATH, '//div[text()="Дубровка"]')
    NEXT_BUTTON = (By.XPATH, '//button[text()="Далее"]')
    DATE_DELIVER_BUTTON = (By.XPATH, '//input[@placeholder="* Когда привезти самокат"]')
    RENT_DATE_BUTTON = (By.XPATH, '//div[text()="* Срок аренды"]')
    ONE_DAY_RENT = (By.XPATH, '//div[text() = "сутки"]')
    TWO_DAY_RENT = (By.XPATH, '//div[text() = "двое суток"]')
    BLACK_COLOR = (By.XPATH, '//label[@for="black"]')
    GREY_COLOR = (By.XPATH, '//label[@for="grey"]')
    COMMENT_INPUT = (By.XPATH, '//input[@placeholder="Комментарий для курьера"]')
    ORDER_BUTTON = (By.XPATH, '//div[@class = "Order_Buttons__1xGrp"]/button[text()="Заказать"]')
    CONFIRM_ORDER_BUTTON = (By.XPATH, '//button[text()="Да"]')
    SUCCESS_WINDOW = (By.XPATH, '//div[contains(@class,"Order_ModalHeader") and text()="Заказ оформлен"]') 
    CHECK_STATUS_BUTTON = (By.XPATH, '//button[text()="Посмотреть статус"]')
    
    
