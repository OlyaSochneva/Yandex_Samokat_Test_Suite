import pytest
import allure

from pages.main_page import MainPage
from pages.order_page import OrderPage

from locators.order_page_locators import OrderPageLocators as Order

from data import TestUser
from data import ErrorMessage
from validation_test_data import Surname


class TestSurnameInput:
    @allure.title('Фамилия: допустимые по требованиям значения проходят валидацию, можно перейти на сл стр,'
                  'поле подсвечивается черным, сообщение о некорректном вводе не появляется')
    @pytest.mark.parametrize('driver, surname',
                             [('chrome', surname) for surname in Surname.VALID]
                             +
                             [('firefox', surname) for surname in Surname.VALID])
    def test_surname_field_valid_input(self, request, driver, surname):
        driver = request.getfixturevalue(driver)
        main_page, order_page = MainPage(driver), OrderPage(driver)
        data = {**TestUser.ALL_FIELDS, "surname": surname}
        main_page.click_on_order_button()
        order_page.who_orders_fill_fields(data)
        result = order_page.check_highlight_and_error_message(Order.SURNAME_INPUT, ErrorMessage.SURNAME)
        next_page = order_page.click_next_button_and_check_next_page_displayed()
        assert (next_page == "page displayed" and result == "Black highlight, no error message"), \
            (f"\n"
             f"Expected 'Black highlight, no error message', but got '{result}'\n"
             f"Expected 'page displayed', but got '{next_page}'")

    @allure.title('Фамилия: если ввести некорректное значение, нельзя перейти на сл страницу, '
                  'поле подсвечивается красным и появляется надпись «Введите корректную фамилию»')
    @pytest.mark.parametrize('driver, surname',
                             [('chrome', surname) for surname in Surname.INVALID]
                             +
                             [('firefox', surname) for surname in Surname.INVALID])
    def test_surname_field_invalid_input(self, request, driver, surname):
        driver = request.getfixturevalue(driver)
        main_page, order_page = MainPage(driver), OrderPage(driver)
        data = {**TestUser.ALL_FIELDS, "surname": surname}
        main_page.click_on_order_button()
        order_page.who_orders_fill_fields(data)
        result = order_page.check_highlight_and_error_message(Order.SURNAME_INPUT, ErrorMessage.SURNAME)
        next_page = order_page.click_next_button_and_check_next_page_displayed()
        assert (next_page == "page not displayed" and result == "Red highlight and error message"), \
            (f"\n"
             f"Expected 'Red highlight and error message', but got '{result}'\n"
             f"Expected 'page not displayed', but got '{next_page}'")
