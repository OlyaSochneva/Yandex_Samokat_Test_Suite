import pytest
import allure

from pages.common_header import CommonHeader
from pages.main_page import MainPage
from pages.order_page import OrderPage


class TestCommonHeader:

    @allure.title('Проверка: переход на страницу заказа при нажатии на кнопку «Заказать» в хэдере')
    @pytest.mark.parametrize('driver',
                             ['chrome', 'firefox'])
    def test_move_by_click_on_header_order_button(self, request, driver):
        driver = request.getfixturevalue(driver)
        common_header, order_page = CommonHeader(driver), OrderPage(driver)
        common_header.click_on_order_button()
        assert order_page.who_orders_page_is_displayed() == "page displayed"

    @allure.title('Проверка: при нажатии на лого Яндекса в новом окне откроется главная Дзена')
    @pytest.mark.parametrize("driver", ['chrome', 'firefox'])
    def test_redirect_by_click_on_yandex_logo(self, request, driver):
        driver = request.getfixturevalue(driver)
        common_header = CommonHeader(driver)
        common_header.click_on_yandex_logo_and_switch_to_new_window()
        assert common_header.dzen_main_page_is_displayed() == "page displayed"

    @allure.title('Проверка: при нажатии на лого Самоката произойдёт переход на главную страницу')
    @pytest.mark.parametrize("driver", ['chrome', 'firefox'])
    def test_return_to_main_page_by_click_on_scooter_logo(self, request, driver):
        driver = request.getfixturevalue(driver)
        common_header, main_page = CommonHeader(driver), MainPage(driver)
        common_header.click_on_order_button()
        common_header.return_to_main_page_by_click_on_logo()
        assert main_page.main_page_is_displayed() == "page displayed"

    @allure.title('Проверка: если ввести в поиске сущ. номер заказа, откроется страница статуса этого заказа')
    @pytest.mark.parametrize("driver", ['chrome', 'firefox'])
    def test_move_to_order_status_page_by_search_field(self, request, driver, create_order_and_return_track):
        driver = request.getfixturevalue(driver)
        common_header = CommonHeader(driver)
        order_number = create_order_and_return_track
        common_header.find_order(order_number)
        assert common_header.status_page_is_displayed() == "page displayed"
