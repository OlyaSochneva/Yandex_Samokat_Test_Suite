import pytest
import allure

from tests.tests_validation.base_test import BaseTest as Base

from locators.order_page_locators import OrderPageLocators as Order

from data import TestUser
from data import ErrorMessage
from validation_test_data import Phone


class TestPhoneInput(Base):
    @allure.title('Телефон: допустимые по требованиям значения проходят валидацию, можно перейти на сл стр,'
                  'поле подсвечивается черным, сообщение о некорректном вводе не появляется')
    @pytest.mark.parametrize('driver, phone',
                             [('chrome', phone) for phone in Phone.VALID]
                             +
                             [('firefox', phone) for phone in Phone.VALID])
    def test_phone_field_valid_input(self, request, driver, phone):
        driver = request.getfixturevalue(driver)
        data = {**TestUser.ALL_FIELDS, "phone": phone}
        self.validate_input_field(driver, data, Order.PHONE_INPUT, ErrorMessage.PHONE,
                                  expected_highlight="Black",
                                  expected_error_message="no error message",
                                  expected_next_page="page displayed")

    @allure.title('Телефон: если ввести некорректное значение, нельзя перейти на сл страницу, '
                  'поле подсвечивается красным и появляется надпись «Введите корректный телефон»')
    @pytest.mark.parametrize('driver, phone',
                             [('chrome', phone) for phone in Phone.INVALID]
                             +
                             [('firefox', phone) for phone in Phone.INVALID])
    def test_phone_field_invalid_input(self, request, driver, phone):
        driver = request.getfixturevalue(driver)
        data = {**TestUser.ALL_FIELDS, "phone": phone}
        self.validate_input_field(driver, data, Order.PHONE_INPUT, ErrorMessage.PHONE,
                                  expected_highlight="Red",
                                  expected_error_message="error message",
                                  expected_next_page="page not displayed")
