import pytest
import allure
import itertools

from locators.order_page_locators import OrderPageLocators as Order
from input_data import Phone
from data import TestUser, ErrorMessage
from soft_assert import check, verify


class TestPhoneInput:
    @allure.title('Если ввести корректный телефон, можно перейти на сл стр')
    @pytest.mark.parametrize('driver, phone', itertools.product(["chrome", "firefox"], Phone.VALID))
    def test_phone_field_valid_input(self, driver, main_page, order_page, phone):
        data = {**TestUser.ALL_FIELDS, "phone": phone}
        main_page.click_on_order_button()
        order_page.first_order_page_fill_fields_and_next(data)
        assert order_page.is_second_order_page_displayed() == "displayed"

    @allure.title('Если ввести некорректный телефон, нельзя перейти на сл страницу,'
                  'поле подсвечивается красным и появляется надпись «Введите корректный номер')
    @pytest.mark.parametrize('driver, phone', itertools.product(["chrome", "firefox"], Phone.INVALID))
    def test_phone_field_invalid_input_shows_error(self, driver, main_page, order_page, phone):
        data = {**TestUser.ALL_FIELDS, "phone": phone}
        main_page.click_on_order_button()
        order_page.first_order_page_fill_fields_and_next(data)
        next_page = order_page.is_second_order_page_displayed()
        highlight = order_page.check_red_highlight(Order.PHONE_INPUT)
        error_message = order_page.check_error_message(Order.PHONE_INPUT)
        with verify():
            check(next_page == "not displayed", f"expected next page: not displayed, actual: '{next_page}' ")
            check(highlight == "Red", f"expected highlight: Red, actual: '{highlight}' ")
            check(error_message == "Введите корректный номер",
                  f"Expected message: 'Введите корректный номер' actual: '{error_message}' ")


