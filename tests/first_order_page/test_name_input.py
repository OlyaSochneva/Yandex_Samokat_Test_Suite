import pytest
import allure
import itertools

from locators.order_page_locators import OrderPageLocators as Order
from input_data import Name
from data import TestUser, ErrorMessage
from soft_assert import check, verify


class TestNameInput:
    @allure.title('Если ввести корректное имя, можно перейти на сл стр')
    @pytest.mark.parametrize('driver, name', itertools.product(["chrome", "firefox"], Name.VALID))
    def test_name_field_valid_input(self, driver, main_page, order_page, name):
        data = {**TestUser.ALL_FIELDS, "name": name}
        main_page.click_on_order_button()
        order_page.first_order_page_fill_fields_and_next(data)
        assert order_page.is_second_order_page_displayed() == "displayed"

    @allure.title('Если ввести некорректное имя, нельзя перейти на сл страницу, '
                  'поле подсвечивается красным и появляется надпись «Введите корректное имя»')
    @pytest.mark.parametrize('driver, name', itertools.product(["chrome", "firefox"], Name.INVALID))
    def test_name_field_invalid_input_shows_error(self, driver, main_page, order_page, name):
        data = {**TestUser.ALL_FIELDS, "name": name}
        main_page.click_on_order_button()
        order_page.first_order_page_fill_fields_and_next(data)
        next_page = order_page.is_second_order_page_displayed()
        highlight = order_page.check_red_highlight(Order.NAME_INPUT)
        error_message = order_page.check_error_message(Order.NAME_INPUT)
        with verify():
            check(next_page == "not displayed", f"expected next page: not displayed, actual: '{next_page}' ")
            check(highlight == "Red", f"expected highlight: Red, actual: '{highlight}' ")
            check(error_message == "Введите корректное имя",
                  f"Expected message: 'Введите корректное имя' actual: '{error_message}' ")


















