import pytest
import allure
import itertools

from locators.order_page_locators import OrderPageLocators as Order
from input_data import RentalTerm
from data import TestUser
from soft_assert import check, verify


class TestRentalTermSelectBox:
    @pytest.mark.parametrize('driver, term', itertools.product(["chrome", "firefox"], RentalTerm.VALID))
    @allure.title('Любой срок аренды из списка можно выбрать')
    def test_selection_rental_term_from_list(self, driver, main_page, order_page, term):
        data = {**TestUser.ALL_FIELDS, "rental_term": term}
        main_page.click_on_order_button()
        order_page.fill_all_fields(data)
        actual_value = order_page.return_rental_term_select_box_value()
        order_page.click_order_button()
        confirm_popup = order_page.check_confirmation_popup_displayed()
        with verify():
            check(actual_value == term, f"expected value: '{term}', actual: '{actual_value}' ")
            check(confirm_popup == "displayed", f"expected confirm_popup: displayed, actual: '{confirm_popup}'")

    @allure.title('Если не выбрать срок аренды, нельзя перейти к подтверждению заказа')
    @pytest.mark.parametrize("driver", ['chrome', 'firefox'])
    def test_leaving_rental_term_unfilled_shows_error(self, driver, main_page, order_page):
        data = {key: value for key, value in TestUser.ALL_FIELDS.items() if key != "rental_term"}
        main_page.click_on_order_button()
        order_page.fill_all_fields_and_order(data)
        confirm_popup = order_page.check_confirmation_popup_displayed()
        highlight = order_page.check_red_highlight(Order.RENTAL_TERM_SELECT_BOX)
        with verify():
            check(confirm_popup == "not displayed",
                  f"expected confirm_popup: not displayed, actual: '{confirm_popup}' ")
            check(highlight == "Red", f"expected highlight: Red, actual: '{highlight}' ")


