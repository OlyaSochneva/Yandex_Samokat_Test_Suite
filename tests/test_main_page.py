import pytest
import allure

from pages.main_page import MainPage
from pages.order_page import OrderPage

from data import Questions
from data import Answers


class TestMainPage:
    @allure.title('Проверка: переход на страницу заказа при нажатии на кнопку «Заказать» на гл. стр')
    @pytest.mark.parametrize('driver',
                             ['chrome', 'firefox'])
    def test_move_by_click_main_page_order_button(self, request, driver):
        driver = request.getfixturevalue(driver)
        main_page, order_page = MainPage(driver), OrderPage(driver)
        main_page.click_on_order_button()
        assert order_page.who_orders_page_is_displayed() == "page displayed"

    @allure.title('Проверка: у вопроса правильный текст')
    @pytest.mark.parametrize(
        "driver, number, expected_text",
        [
            ('chrome', 0, Questions.COST_AND_PAYMENT),
            ('chrome', 1, Questions.MORE_SCOOTERS),
            ('chrome', 2, Questions.RENTAL_TIME),
            ('chrome', 3, Questions.TODAY_DELIVERY),
            ('chrome', 4, Questions.EXTEND_RETURN),
            ('chrome', 5, Questions.ABOUT_CHARGER),
            ('chrome', 6, Questions.CANCEL_ORDER),
            ('chrome', 7, Questions.FAR_AWAY_DELIVERY),
            ('firefox', 0, Questions.COST_AND_PAYMENT),
            ('firefox', 1, Questions.MORE_SCOOTERS),
            ('firefox', 2, Questions.RENTAL_TIME),
            ('firefox', 3, Questions.TODAY_DELIVERY),
            ('firefox', 4, Questions.EXTEND_RETURN),
            ('firefox', 5, Questions.ABOUT_CHARGER),
            ('firefox', 6, Questions.CANCEL_ORDER),
            ('firefox', 7, Questions.FAR_AWAY_DELIVERY)
        ])
    def test_questions_text_is_correct(self, request, driver, number, expected_text):
        driver = request.getfixturevalue(driver)
        main_page = MainPage(driver)
        result = main_page.get_question_text(number)
        assert result == expected_text

    @allure.title('Проверка: при нажатии на вопрос появляется правильный текст ответа')
    @pytest.mark.parametrize(
        "driver, number, expected_text",
        [
            ('chrome', 0, Answers.COST_AND_PAYMENT),
            ('chrome', 1, Answers.MORE_SCOOTERS),
            ('chrome', 2, Answers.RENTAL_TIME),
            ('chrome', 3, Answers.TODAY_DELIVERY),
            ('chrome', 4, Answers.EXTEND_RETURN),
            ('chrome', 5, Answers.ABOUT_CHARGER),
            ('chrome', 6, Answers.CANCEL_ORDER),
            ('chrome', 7, Answers.FAR_AWAY_DELIVERY),
            ('firefox', 0, Answers.COST_AND_PAYMENT),
            ('firefox', 1, Answers.MORE_SCOOTERS),
            ('firefox', 2, Answers.RENTAL_TIME),
            ('firefox', 3, Answers.TODAY_DELIVERY),
            ('firefox', 4, Answers.EXTEND_RETURN),
            ('firefox', 5, Answers.ABOUT_CHARGER),
            ('firefox', 6, Answers.CANCEL_ORDER),
            ('firefox', 7, Answers.FAR_AWAY_DELIVERY)
        ])
    def test_answers_text_is_correct(self, request, driver, number, expected_text):
        driver = request.getfixturevalue(driver)
        main_page = MainPage(driver)
        result = main_page.click_on_question_and_get_answer_text(number)
        assert result == expected_text


