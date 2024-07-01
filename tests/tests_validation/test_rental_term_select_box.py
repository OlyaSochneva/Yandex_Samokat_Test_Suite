import pytest
import allure

from pages.main_page import MainPage
from pages.order_page import OrderPage

from locators.order_page_locators import OrderPageLocators as Order

from data import TestUser
from validation_test_data import RentalTerm


class TestRentalTermSelectBox:
    @pytest.mark.parametrize('driver, term',
                             [('firefox', term) for term in RentalTerm.VALID]
                             +
                             [('chrome', term) for term in RentalTerm.VALID])
    @allure.title('Проверка: любой срок аренды из списка можно выбрать')
    def test_selection_rental_term_from_list(self, request, driver, term):
        driver = request.getfixturevalue(driver)
        main_page, order_page = MainPage(driver), OrderPage(driver)
        data = {**TestUser.ALL_FIELDS, "rental_term": term}
        main_page.click_on_order_button()
        order_page.fill_all_fields(data)
        result = order_page.return_rental_term_select_box_value()
        next_page = order_page.click_order_button_and_check_confirmation_popup_displayed()
        assert (result == term and next_page == "page displayed"), \
            (f"\n"
             f"Expected '{term}', but got '{result}'\n"
             f"Expected 'page displayed', but got '{next_page}'")

    @allure.title('Проверка: если оставить поле незаполненным, нельзя оформить заказ')
    @pytest.mark.parametrize('driver', ['chrome', 'firefox'])
    def test_leaving_rental_term_unfilled_shows_error(self, request, driver):
        driver = request.getfixturevalue(driver)
        main_page, order_page = MainPage(driver), OrderPage(driver)
        data = {key: value for key, value in TestUser.ALL_FIELDS.items() if key != "rental_term"}
        main_page.click_on_order_button()
        order_page.fill_all_fields(data)
        highlight = order_page.check_highlight(Order.RENTAL_TERM_SELECT_BOX)
        next_page = order_page.click_order_button_and_check_confirmation_popup_displayed()
        assert (next_page == "page not displayed" and highlight == "Red"), \
            (f"\n"
             f"Expected 'Red', but got '{highlight}'\n"
             f"Expected 'page not displayed', but got '{next_page}'")
