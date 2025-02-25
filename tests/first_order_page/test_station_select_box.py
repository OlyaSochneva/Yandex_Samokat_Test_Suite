import pytest
import allure
import itertools

from locators.order_page_locators import OrderPageLocators as Order
from input_data import Station
from data import TestUser
from soft_assert import check, verify


class TestStationSelectBox:
    @allure.title('Можно выбрать станции из списка и перейти на сл страницу')
    @pytest.mark.parametrize('driver, station', itertools.product(["chrome", "firefox"], Station.VALID))
    def test_selection_station_from_list(self, driver, main_page, order_page, station):
        data = {**TestUser.ALL_FIELDS, "station": station}
        main_page.click_on_order_button()
        order_page.first_order_page_fill_fields(data)
        actual_value = order_page.return_station_field_value()
        order_page.click_next_button()
        next_page = order_page.is_second_order_page_displayed()
        with verify():
            check(actual_value == station, f"expected value: '{station}', actual: '{actual_value}' ")
            check(next_page == "displayed", f"expected next page: displayed, actual: '{next_page}' ")

    @allure.title('Полю «Станция метро» нельзя задать своё значение')
    @pytest.mark.parametrize("driver", ['chrome', 'firefox'])
    def test_station_input_clear_on_blur_without_list_selection(self, driver, main_page, order_page):
        main_page.click_on_order_button()
        order_page.fill_station_field_manually("Петроградская")
        actual_value = order_page.return_station_field_value()
        assert actual_value == ""

    @allure.title('Станция метро: если оставить поле пустым, нельзя перейти на сл страницу,'
                  'поле подсветится красным и появится надпись «Выберите станцию»')
    @pytest.mark.parametrize("driver", ['chrome', 'firefox'])
    def test_leaving_station_field_unfilled_shows_error(self, driver, main_page, order_page):
        data = {key: value for key, value in TestUser.ALL_FIELDS.items() if key != "station"}
        main_page.click_on_order_button()
        order_page.first_order_page_fill_fields_and_next(data)
        next_page = order_page.is_second_order_page_displayed()
        highlight = order_page.check_red_highlight(Order.STATION_SELECT_BOX)
        error_message = order_page.check_error_message(Order.STATION_SELECT_BOX)
        with verify():
            check(next_page == "not displayed", f"expected next page: not displayed, actual: '{next_page}' ")
            check(highlight == "Red", f"expected highlight: Red, actual: '{highlight}' ")
            check(error_message == "Выберите станцию",
                  f"Expected message: 'Выберите станцию' actual: '{error_message}' ")
