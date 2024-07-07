import pytest
import allure
from utils.test_data import YaScooterAnswersFAQ
from pages.main_page import YaScooterMainPage
from locators.main_page_locators import MainPageLocators


class TestYaScooterFAQPage:
    @pytest.mark.parametrize(
        'question, answer, expected_text',
        [
            (MainPageLocators.FAQ_Q_1, MainPageLocators.FAQ_A_1, YaScooterAnswersFAQ.answer_1),
            (MainPageLocators.FAQ_Q_2, MainPageLocators.FAQ_A_2, YaScooterAnswersFAQ.answer_2),
            (MainPageLocators.FAQ_Q_3, MainPageLocators.FAQ_A_3, YaScooterAnswersFAQ.answer_3),
            (MainPageLocators.FAQ_Q_4, MainPageLocators.FAQ_A_4, YaScooterAnswersFAQ.answer_4),
            (MainPageLocators.FAQ_Q_5, MainPageLocators.FAQ_A_5, YaScooterAnswersFAQ.answer_5),
            (MainPageLocators.FAQ_Q_6, MainPageLocators.FAQ_A_6, YaScooterAnswersFAQ.answer_6),
            (MainPageLocators.FAQ_Q_7, MainPageLocators.FAQ_A_7, YaScooterAnswersFAQ.answer_7),
            (MainPageLocators.FAQ_Q_8, MainPageLocators.FAQ_A_8, YaScooterAnswersFAQ.answer_8)
            ]
        )
    @allure.title('Проверка, что ответы соответствуют вопросам')
    @allure.description('На странице находим вопрос, нажимаем на него, открывается ответ, сверяем с нужным ответом')
    def test_answer_to_questions(self, driver, question, answer, expected_text):
        main_page = YaScooterMainPage(driver)
        main_page.go_to_site()
        main_page.click_accept_cookies()
        main_page.click_faq_question(question)
        answer_texts = main_page.get_answer_text(answer)
        assert answer_texts == expected_text