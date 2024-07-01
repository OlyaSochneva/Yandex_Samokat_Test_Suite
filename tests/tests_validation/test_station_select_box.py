import pytest
import allure

from pages.main_page import MainPage
from pages.order_page import OrderPage

from locators.order_page_locators import OrderPageLocators as Order

from data import TestUser
from data import ErrorMessage
from validation_test_data import Station


class TestStationSelectBox:
    @allure.title('Проверка: можно выбрать станцию из списка')
    @pytest.mark.parametrize('driver, station',
                             [('chrome', station) for station in Station.VALID]
                             +
                             [('firefox', station) for station in Station.VALID])
    def test_selection_station_from_list(self, request, driver, station):
        driver = request.getfixturevalue(driver)
        main_page, order_page = MainPage(driver), OrderPage(driver)
        data = {**TestUser.ALL_FIELDS, "station": station}
        main_page.click_on_order_button()
        order_page.who_orders_fill_fields(data)
        result = order_page.return_station_field_value()
        next_page = order_page.click_next_button_and_check_next_page_displayed()
        assert (result == station and next_page == "page displayed"), \
            (f"\n"
             f"Expected '{station}', but got '{result}'\n"
             f"Expected 'page displayed', but got '{next_page}'")

    @allure.title('Проверка: полю «Станция метро» нельзя задать своё значение')
    @pytest.mark.parametrize('driver, station',
                             [('chrome', station) for station in Station.INVALID]
                             +
                             [('firefox', station) for station in Station.INVALID])
    def test_station_input_clear_on_blur_without_list_selection(self, request, driver, station):
        driver = request.getfixturevalue(driver)
        main_page, order_page = MainPage(driver), OrderPage(driver)
        main_page.click_on_order_button()
        order_page.fill_station_field_manually(station)
        result = order_page.return_station_field_value()
        assert result == ""

    @allure.title('Станция метро: если оставить поле пустым, нельзя перейти на сл страницу,поле подсветится красным '
                  'и появится надпись «Выберите станцию»')
    @pytest.mark.parametrize('driver', ['firefox', 'chrome'])
    def test_leaving_station_field_unfilled_shows_error(self, request, driver):
        driver = request.getfixturevalue(driver)
        main_page, order_page = MainPage(driver), OrderPage(driver)
        data = {key: value for key, value in TestUser.ALL_FIELDS.items() if key != "station"}
        main_page.click_on_order_button()
        order_page.who_orders_fill_fields(data)
        next_page = order_page.click_next_button_and_check_next_page_displayed()
        result = order_page.check_highlight_and_error_message(Order.STATION_SELECT_BOX, ErrorMessage.STATION)
        assert (next_page == "page not displayed" and result == "Red highlight and error message"), \
            (f"\n"
             f"Expected 'Red highlight and error message', but got '{result}'\n"
             f"Expected 'page not displayed', but got '{next_page}'")
