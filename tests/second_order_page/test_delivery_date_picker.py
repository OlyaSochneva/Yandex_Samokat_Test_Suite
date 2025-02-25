import pytest
import allure
import itertools

from locators.order_page_locators import OrderPageLocators as Order
from input_data import DeliveryDate
from data import TestUser
from soft_assert import check, verify


class TestDeliveryDatePicker:
    @allure.title('Можно выбрать дату доставки, начиная с завтра')
    @pytest.mark.parametrize('driver, date', itertools.product(["chrome", "firefox"], DeliveryDate.VALID))
    def test_delivery_date_valid_input(self, driver, main_page, order_page, date):
        data = {**TestUser.ALL_FIELDS, "delivery_date": date}
        main_page.click_on_order_button()
        order_page.fill_all_fields(data)
        actual_value = order_page.return_delivery_date_picker_value()
        order_page.click_order_button()
        confirm_popup = order_page.check_confirmation_popup_displayed()
        with verify():
            check(actual_value == date, f"expected value: '{date}', actual: '{actual_value}' ")
            check(confirm_popup == "displayed", f"expected confirm_popup: displayed, actual: '{confirm_popup}'")

    @allure.title('Если выбрать некорректную дату доставки (или не указывать), нельзя перейти к подтверждению заказа')
    @pytest.mark.parametrize('driver, date', itertools.product(["chrome", "firefox"], DeliveryDate.INVALID))
    def test_delivery_date_invalid_input_shows_error(self, driver, main_page, order_page, date):
        data = {**TestUser.ALL_FIELDS, "delivery_date": date}
        main_page.click_on_order_button()
        order_page.fill_all_fields_and_order(data)
        confirm_popup = order_page.check_confirmation_popup_displayed()
        highlight = order_page.check_red_highlight(Order.RENTAL_TERM_SELECT_BOX)
        with verify():
            check(confirm_popup == "not displayed",
                  f"expected confirm_popup: not displayed, actual: '{confirm_popup}' ")
            check(highlight == "Red", f"expected highlight: Red, actual: '{highlight}' ")

