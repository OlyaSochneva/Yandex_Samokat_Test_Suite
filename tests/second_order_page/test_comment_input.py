import pytest
import allure
import itertools

from locators.order_page_locators import OrderPageLocators as Order
from input_data import Comment
from data import TestUser
from soft_assert import check, verify


class TestCommentInput:
    @allure.title('Если ввести корректный комментарий, можно перейти к подтверждению заказа')
    @pytest.mark.parametrize('driver, comment', itertools.product(["chrome", "firefox"], Comment.VALID))
    def test_comment_field_valid_input(self, driver, main_page, order_page, comment):
        data = {**TestUser.ALL_FIELDS, "comment": comment}
        main_page.click_on_order_button()
        order_page.fill_all_fields_and_order(data)
        confirm_popup = order_page.check_confirmation_popup_displayed()
        assert confirm_popup == "displayed"

    @allure.title('Если ввести некорректный комментарий, нельзя перейти к подтверждению заказа,'
                  'поле подсвечивается красным')
    @pytest.mark.parametrize('driver, comment', itertools.product(["chrome", "firefox"], Comment.INVALID))
    def test_comment_field_invalid_input_shows_error(self, driver, main_page, order_page, comment):
        data = {**TestUser.ALL_FIELDS, "comment": comment}
        main_page.click_on_order_button()
        order_page.fill_all_fields_and_order(data)
        confirm_popup = order_page.check_confirmation_popup_displayed()
        highlight = order_page.check_red_highlight(Order.COMMENT_INPUT)
        with verify():
            check(confirm_popup == "not displayed",
                  f"expected confirm_popup: not displayed, actual: '{confirm_popup}' ")
            check(highlight == "Red", f"expected highlight: Red, actual: '{highlight}' ")
