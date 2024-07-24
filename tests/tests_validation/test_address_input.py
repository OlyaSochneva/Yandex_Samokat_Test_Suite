import pytest
import allure

from tests.tests_validation.base_test import BaseTest as Base

from locators.order_page_locators import OrderPageLocators as Order

from data import TestUser
from data import ErrorMessage
from validation_test_data import Address


class TestAddressInput(Base):
    @allure.title('Адрес: допустимые по требованиям значения проходят валидацию, можно перейти на сл стр, '
                  'поле подсвечивается черным, сообщение о некорректном вводе не появляется')
    @pytest.mark.parametrize('driver, address',
                             [('chrome', address) for address in Address.VALID]
                             +
                             [('firefox', address) for address in Address.VALID])
    def test_address_field_valid_input(self, request, driver, address):
        driver = request.getfixturevalue(driver)
        data = {**TestUser.ALL_FIELDS, "address": address}
        self.validate_input_field(driver, data, Order.ADDRESS_INPUT, ErrorMessage.ADDRESS,
                                  expected_highlight="Black",
                                  expected_error_message="no error message",
                                  expected_next_page="page displayed")

    @allure.title('Адрес: если ввести некорректное значение, нельзя перейти на сл страницу, '
                  'поле подсвечивается красным и появляется надпись «Введите корректный адрес»')
    @pytest.mark.parametrize('driver, address',
                             [('chrome', address) for address in Address.INVALID]
                             +
                             [('firefox', address) for address in Address.INVALID])
    def test_address_field_invalid_input(self, request, driver, address):
        driver = request.getfixturevalue(driver)
        data = {**TestUser.ALL_FIELDS, "address": address}
        self.validate_input_field(driver, data, Order.ADDRESS_INPUT, ErrorMessage.ADDRESS,
                                  expected_highlight="Red",
                                  expected_error_message="error message",
                                  expected_next_page="page not displayed")



