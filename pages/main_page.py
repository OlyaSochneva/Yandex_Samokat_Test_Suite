import allure

from pages.base_page import BasePage
from locators.main_page_locators import MainPageLocators as Main


class MainPage(BasePage):
    @allure.step("Проверяем что открыта главная страница")
    def main_page_is_displayed(self):
        return self.check_page_displayed(Main.ORDER_BUTTON)

    @allure.step("Клик на кнопку «Заказать» на главной странице")
    def click_on_order_button(self):
        self.scroll_to_element(Main.ORDER_BUTTON)
        self.click_element(Main.ORDER_BUTTON)

    @allure.step("Получить текст вопроса")
    def get_question_text(self, number):
        question = self.create_question_locator(number)
        self.scroll_to_element(question)
        return self.get_text(question)

    @allure.step("Кликаем на вопрос и получаем текст ответа")
    def click_on_question_and_get_answer_text(self, number):
        question = self.create_question_locator(number)
        self.scroll_to_element(question)
        self.click_element(question)
        answer = self.create_answer_locator(number)
        return self.get_text(answer)

    @allure.step("Создаем локатор вопроса")
    def create_question_locator(self, number):
        return self.create_locator(Main.QUESTION_TEMPLATE, number)

    @allure.step("Создаем локатор ответа")
    def create_answer_locator(self, number):
        return self.create_locator(Main.ANSWER_TEMPLATE, number)