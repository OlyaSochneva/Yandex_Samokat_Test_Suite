import pytest
import allure

from pages.main_page import MainPage
from pages.order_page import OrderPage

from locators.order_page_locators import OrderPageLocators as Order

from validation_test_data import DeliveryDate
from data import TestUser


class TestDeliveryDatePicker:
    @allure.title('Проверка: можно выбрать предстоящую дату, начиная с завтра')
    @pytest.mark.parametrize('driver, date',
                             [('chrome', date) for date in DeliveryDate.VALID]
                             +
                             [('firefox', date) for date in DeliveryDate.VALID])
    def test_valid_delivery_date(self, request, driver, date):
        driver = request.getfixturevalue(driver)
        main_page, order_page = MainPage(driver), OrderPage(driver)
        data = {**TestUser.ALL_FIELDS, "delivery_date": date}
        main_page.click_on_order_button()
        order_page.fill_all_fields(data)
        highlight = order_page.check_highlight(Order.DELIVERY_DATE_PICKER)
        next_page = order_page.click_order_button_and_check_confirmation_popup_displayed()
        assert (next_page == "page displayed" and highlight == "Black"), \
            (f"\n"
             f"Expected 'Black', but got '{highlight}'\n"
             f"Expected 'page displayed', but got '{next_page}'")

    @allure.title('Дата: если ввести некорректное значение, нельзя перейти на сл страницу, '
                  'поле подсвечивается красным и появляется сообщение об ошибке')
    @pytest.mark.parametrize('driver, date',
                             [('chrome', date) for date in DeliveryDate.INVALID]
                             +
                             [('firefox', date) for date in DeliveryDate.INVALID])
    def test_invalid_delivery_date(self, request, driver, date):
        driver = request.getfixturevalue(driver)
        main_page, order_page = MainPage(driver), OrderPage(driver)
        data = {**TestUser.ALL_FIELDS, "delivery_date": date}
        main_page.click_on_order_button()
        order_page.fill_all_fields(data)
        highlight = order_page.check_highlight(Order.DELIVERY_DATE_PICKER)
        next_page = order_page.click_order_button_and_check_confirmation_popup_displayed()
        assert (next_page == "page not displayed" and highlight == "Red"), \
            (f"\n"
             f"Expected 'Red', but got '{highlight}'\n"
             f"Expected 'page not displayed', but got '{next_page}'")

