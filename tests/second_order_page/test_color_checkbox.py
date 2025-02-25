import pytest
import allure
import itertools

from input_data import Color
from data import TestUser


class TestColorCheckbox:
    @pytest.mark.parametrize('driver, color', itertools.product(["chrome", "firefox"], Color.VALID))
    @allure.title('Можно выбрать один цвет, оба или не указывать вообще')
    def test_selection_colors_from_list(self, driver, main_page, order_page, color):
        data = {**TestUser.ALL_FIELDS, "color": color}
        main_page.click_on_order_button()
        order_page.fill_all_fields_and_order(data)
        assert order_page.check_confirmation_popup_displayed() == "displayed"
