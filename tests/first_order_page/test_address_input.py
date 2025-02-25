import pytest
import allure
import itertools

from locators.order_page_locators import OrderPageLocators as Order
from input_data import Address
from data import TestUser
from soft_assert import check, verify


class TestAddressInput:
    @allure.title('Если ввести корректный адрес, можно перейти на сл стр')
    @pytest.mark.parametrize('driver, address', itertools.product(["chrome", "firefox"], Address.VALID))
    def test_address_field_valid_input(self, driver, main_page, order_page, address):
        data = {**TestUser.ALL_FIELDS, "address": address}
        main_page.click_on_order_button()
        order_page.first_order_page_fill_fields_and_next(data)
        assert order_page.is_second_order_page_displayed() == "displayed"

    @allure.title('Если ввести некорректный адрес, нельзя перейти на сл страницу, '
                  'поле подсвечивается красным и появляется надпись «Введите корректный адрес»')
    @pytest.mark.parametrize('driver, address', itertools.product(["chrome", "firefox"], Address.INVALID))
    def test_address_field_invalid_input_shows_error(self, driver, main_page, order_page, address):
        data = {**TestUser.ALL_FIELDS, "address": address}
        main_page.click_on_order_button()
        order_page.first_order_page_fill_fields_and_next(data)
        next_page = order_page.is_second_order_page_displayed()
        highlight = order_page.check_red_highlight(Order.ADDRESS_INPUT)
        error_message = order_page.check_error_message(Order.ADDRESS_INPUT)
        with verify():
            check(next_page == "not displayed", f"expected next page: not displayed, actual: '{next_page}' ")
            check(highlight == "Red", f"expected highlight: Red, actual: '{highlight}' ")
            check(error_message == "Введите корректный адрес",
                  f"Expected message: 'Введите корректный адрес' actual: '{error_message}' ")
