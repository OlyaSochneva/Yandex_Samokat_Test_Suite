import pytest
import allure

from pages.main_page import MainPage
from pages.order_page import OrderPage

from data import TestUser
from assistant_methods import compare_values


class TestOrderPage:
    @allure.title('Проверка: при прохождении всего позитивного сценария с корректными данными заказ успешно создаётся')
    @pytest.mark.parametrize('driver', ['chrome', 'firefox'])
    def test_create_order_with_valid_data(self, request, driver):
        driver = request.getfixturevalue(driver)
        main_page, order_page = MainPage(driver), OrderPage(driver)
        main_page.click_on_order_button()
        order_page.create_order(TestUser.ALL_FIELDS)
        assert order_page.order_created_popup_is_displayed() == "page displayed"

    @allure.title('Проверка: на стр «Для кого самокат» введённая информация сохраняется при возврате')
    @pytest.mark.parametrize('driver', ['chrome', 'firefox'])
    def test_who_orders_page_fields_values_does_not_clear(self, request, driver):
        driver = request.getfixturevalue(driver)
        main_page, order_page = MainPage(driver), OrderPage(driver)
        main_page.click_on_order_button()
        order_page.who_orders_fill_fields(TestUser.ALL_FIELDS)
        order_page.click_next_button()
        order_page.click_back_button()
        result = compare_values(order_page.return_who_orders_fields_values(), TestUser.ALL_FIELDS)
        assert result == "values are the same"






