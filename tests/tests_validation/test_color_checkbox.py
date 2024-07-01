import pytest
import allure

from pages.main_page import MainPage
from pages.order_page import OrderPage

from data import TestUser
from validation_test_data import Color


class TestColorCheckbox:
    @pytest.mark.parametrize('driver, color',
                             [('chrome', color) for color in Color.VALID]
                             +
                             [('firefox', color) for color in Color.VALID])
    @allure.title('Проверка: можно выбрать один цвет, оба или не указывать вообще')
    def test_selection_colors_from_list(self, request, driver, color):
        driver = request.getfixturevalue(driver)
        main_page, order_page = MainPage(driver), OrderPage(driver)
        data = {**TestUser.ALL_FIELDS, "color": color}
        main_page.click_on_order_button()
        order_page.fill_all_fields(data)
        next_page = order_page.click_order_button_and_check_confirmation_popup_displayed()
        assert next_page == "page displayed"
