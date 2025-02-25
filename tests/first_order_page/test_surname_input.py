import pytest
import allure
import itertools
from soft_assert import check, verify

from locators.order_page_locators import OrderPageLocators as Order
from input_data import Surname
from data import TestUser, ErrorMessage


class TestSurnameInput:
    @allure.title('Если ввести корректную фамилию, можно перейти на сл стр')
    @pytest.mark.parametrize('driver, surname', itertools.product(["chrome", "firefox"], Surname.VALID))
    def test_surname_field_valid_input(self, driver, main_page, order_page, surname):
        data = {**TestUser.ALL_FIELDS, "surname": surname}
        main_page.click_on_order_button()
        order_page.first_order_page_fill_fields_and_next(data)
        assert order_page.is_second_order_page_displayed() == "displayed"

    @allure.title('Если ввести некорректную фамилию, нельзя перейти на сл страницу,'
                  'поле подсвечивается красным и появляется надпись «Введите корректную фамилию»')
    @pytest.mark.parametrize('driver, surname', itertools.product(["chrome", "firefox"], Surname.INVALID))
    def test_surname_field_invalid_input_shows_error(self, driver, main_page, order_page, surname):
        data = {**TestUser.ALL_FIELDS, "surname": surname}
        main_page.click_on_order_button()
        order_page.first_order_page_fill_fields_and_next(data)
        next_page = order_page.is_second_order_page_displayed()
        highlight = order_page.check_red_highlight(Order.SURNAME_INPUT)
        error_message = order_page.check_error_message(Order.SURNAME_INPUT)
        with verify():
            check(next_page == "not displayed", f"expected next page: not displayed, actual: '{next_page}' ")
            check(highlight == "Red", f"expected highlight: Red, actual: '{highlight}' ")
            check(error_message == "Введите корректную фамилию",
                  f"Expected message: 'Введите корректную фамилию' actual: '{error_message}' ")
