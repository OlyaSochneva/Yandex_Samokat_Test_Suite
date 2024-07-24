import pytest
import allure

from tests.tests_validation.base_test import BaseTest as Base

from locators.order_page_locators import OrderPageLocators as Order

from data import TestUser
from data import ErrorMessage
from validation_test_data import Name


class TestNameInputField(Base):
    @allure.title('Имя: допустимые по требованиям значения проходят валидацию, можно перейти на сл стр,'
                  'поле подсвечивается черным, сообщение о некорректном вводе не появляется')
    @pytest.mark.parametrize('driver, name',
                             [('chrome', name) for name in Name.VALID]
                             +
                             [('firefox', name) for name in Name.VALID])
    def test_name_field_valid_input(self, request, driver, name):
        driver = request.getfixturevalue(driver)
        data = {**TestUser.ALL_FIELDS, "name": name}
        self.validate_input_field(driver, data, Order.NAME_INPUT, ErrorMessage.NAME,
                                  expected_highlight="Black",
                                  expected_error_message="no error message",
                                  expected_next_page="page displayed")

    @allure.title('Имя: если ввести некорректное значение, нельзя перейти на сл страницу, '
                  'поле подсвечивается красным и появляется надпись «Введите корректное имя»')
    @pytest.mark.parametrize('driver, name',
                             [('chrome', name) for name in Name.INVALID]
                             +
                             [('firefox', name) for name in Name.INVALID])
    def test_name_field_invalid_input(self, request, driver, name):
        driver = request.getfixturevalue(driver)
        data = {**TestUser.ALL_FIELDS, "name": name}
        self.validate_input_field(driver, data, Order.NAME_INPUT, ErrorMessage.NAME,
                                  expected_highlight="Red",
                                  expected_error_message="error message",
                                  expected_next_page="page not displayed")
