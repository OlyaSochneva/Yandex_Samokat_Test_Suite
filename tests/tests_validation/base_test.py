import pytest
from pages.main_page import MainPage
from pages.order_page import OrderPage


class BaseTest:
    def validate_input_field(self, driver, data, field_locator, error_locator, expected_highlight,
                             expected_error_message, expected_next_page):
        main_page = MainPage(driver)
        order_page = OrderPage(driver)
        main_page.click_on_order_button()
        order_page.who_orders_fill_fields(data)
        highlight = order_page.check_highlight(field_locator)
        error_message = order_page.check_error_message(error_locator)
        next_page = order_page.click_next_button_and_check_next_page_displayed()
        print(f"\nExpected highlight: '{expected_highlight}', actual: '{highlight}'")
        print(f"Expected error message: '{expected_error_message}', actual: '{error_message}'")
        print(f"Expected next page: '{expected_next_page}', actual: '{next_page}'")
        assert (next_page == expected_next_page and
                highlight == expected_highlight and
                error_message == expected_error_message)
