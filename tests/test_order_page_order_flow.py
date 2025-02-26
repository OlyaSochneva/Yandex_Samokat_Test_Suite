import pytest
import allure
from data import TestUser
from soft_assert import check, verify


class TestOrderPageOrderFlow:
    @allure.title('Если ввести корректные данные, заказ успешно создается')
    @pytest.mark.parametrize("driver", ['chrome', 'firefox'])
    def test_create_order_successfully(self, driver, main_page, order_page):
        main_page.click_on_order_button()
        order_page.create_order_full_flow(TestUser.ALL_FIELDS)
        order_created_popup = order_page.check_order_created_popup_displayed()
        with verify():
            check(order_created_popup == "displayed",
                  f"'{driver}': expected order_created_popup displayed, actual: '{order_created_popup}' ")
