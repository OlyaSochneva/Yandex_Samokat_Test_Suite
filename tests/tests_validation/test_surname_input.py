import pytest
import allure

from tests.tests_validation.base_test import BaseTest as Base

from locators.order_page_locators import OrderPageLocators as Order

from data import TestUser
from data import ErrorMessage
from validation_test_data import Surname


class TestSurnameInput(Base):
    @allure.title('Фамилия: допустимые по требованиям значения проходят валидацию, можно перейти на сл стр,'
                  'поле подсвечивается черным, сообщение о некорректном вводе не появляется')
    @pytest.mark.parametrize('driver, surname',
                             [('chrome', surname) for surname in Surname.VALID]
                             +
                             [('firefox', surname) for surname in Surname.VALID])
    def test_surname_field_valid_input(self, request, driver, surname):
        driver = request.getfixturevalue(driver)
        data = {**TestUser.ALL_FIELDS, "surname": surname}
        self.validate_input_field(driver, data, Order.SURNAME_INPUT, ErrorMessage.SURNAME,
                                  expected_highlight="Black",
                                  expected_error_message="no error message",
                                  expected_next_page="page displayed")

    @allure.title('Фамилия: если ввести некорректное значение, нельзя перейти на сл страницу, '
                  'поле подсвечивается красным и появляется надпись «Введите корректную фамилию»')
    @pytest.mark.parametrize('driver, surname',
                             [('chrome', surname) for surname in Surname.INVALID]
                             +
                             [('firefox', surname) for surname in Surname.INVALID])
    def test_surname_field_invalid_input(self, request, driver, surname):
        driver = request.getfixturevalue(driver)
        data = {**TestUser.ALL_FIELDS, "surname": surname}
        self.validate_input_field(driver, data, Order.SURNAME_INPUT, ErrorMessage.SURNAME,
                                  expected_highlight="Red",
                                  expected_error_message="error message",
                                  expected_next_page="page not displayed")
