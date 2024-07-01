from pages.base_page import BasePage
from locators.main_page_locators import MainPageLocators as Main


class MainPage(BasePage):
    def main_page_is_displayed(self):
        return self.check_page_displayed(Main.ORDER_BUTTON)

    def click_on_order_button(self):
        self.scroll_to_element(Main.ORDER_BUTTON)
        self.click_element(Main.ORDER_BUTTON)

    def get_question_text(self, number):
        question = self.return_question(number)
        return self.get_text(question)

    def click_on_question_and_get_answer_text(self, number):
        question = self.return_question(number)
        self.click_element(question)
        answer = self.create_answer_locator(number)
        return self.get_text(answer)

    def return_question(self, number):
        question_locator = self.create_question_locator(number)
        self.scroll_to_element(question_locator)
        return question_locator

    def create_question_locator(self, number):
        return self.create_locator(Main.QUESTION_TEMPLATE, number)

    def create_answer_locator(self, number):
        return self.create_locator(Main.ANSWER_TEMPLATE, number)