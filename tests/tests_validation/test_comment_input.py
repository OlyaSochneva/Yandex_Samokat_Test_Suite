import pytest
import allure

from pages.main_page import MainPage
from pages.order_page import OrderPage

from locators.order_page_locators import OrderPageLocators as Order

from data import TestUser
from validation_test_data import Comment


class TestCommentInput:
    @allure.title('Комментарий: допустимые по требованиям значения проходят валидацию, поле подсвечивается черным, '
                  'сообщение о некорректном вводе не появляется')
    @pytest.mark.parametrize('driver, comment',
                             [('chrome', comment) for comment in Comment.VALID]
                             +
                             [('firefox', comment) for comment in Comment.VALID])
    def test_comment_valid_input(self, request, driver, comment):
        driver = request.getfixturevalue(driver)
        main_page, order_page = MainPage(driver), OrderPage(driver)
        data = {**TestUser.ALL_FIELDS, "comment": comment}
        main_page.click_on_order_button()
        order_page.fill_all_fields(data)
        highlight = order_page.check_highlight(Order.COMMENT_INPUT)
        next_page = order_page.click_order_button_and_check_confirmation_popup_displayed()
        assert (next_page == "page displayed" and highlight == "Black"), \
            (f"\n"
             f"Expected 'Black', but got '{highlight}'\n"
             f"Expected 'page displayed', but got '{next_page}'")

    @allure.title('Комментарий: если ввести некорректное значение, нельзя перейти на сл страницу, '
                  'поле подсвечивается красным и появляется сообщение об ошибке')
    @pytest.mark.parametrize('driver, comment',
                             [('chrome', comment) for comment in Comment.INVALID]
                             +
                             [('firefox', comment) for comment in Comment.INVALID])
    def test_comment_field_invalid_input(self, request, driver, comment):
        driver = request.getfixturevalue(driver)
        main_page, order_page = MainPage(driver), OrderPage(driver)
        data = {**TestUser.ALL_FIELDS, "comment": comment}
        main_page.click_on_order_button()
        order_page.fill_all_fields(data)
        highlight = order_page.check_highlight(Order.COMMENT_INPUT)
        next_page = order_page.click_order_button_and_check_confirmation_popup_displayed()
        assert (next_page == "page not displayed" and highlight == "Red"), \
            (f"\n"
             f"Expected 'Red', but got '{highlight}'\n"
             f"Expected 'page not displayed', but got '{next_page}'")
