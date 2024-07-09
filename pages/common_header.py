import allure

from pages.base_page import BasePage
from locators.common_header_locators import CommonHeaderLocators as Header


class CommonHeader(BasePage):
    @allure.step("Клик на кнопку «Заказать» в хэдере")
    def click_on_order_button(self):
        self.click_element(Header.HEADER_ORDER_BUTTON)

    @allure.step("Клик на лого «Самокат»")
    def return_to_main_page_by_click_on_logo(self):
        self.click_element(Header.SCOOTER_LOGO)

    @allure.step("Клик на кнопку «Статус заказа»")
    def click_on_order_status_button(self):
        self.click_element(Header.ORDER_STATUS_BUTTON)

    @allure.step("Поиск заказа по номеру")
    def find_order(self, order_number):
        self.click_on_order_status_button()
        self.fill_field(Header.SEARCH_ORDER_INPUT, order_number)
        self.click_element(Header.GO_BUTTON)
        self.pause()

    @allure.step("Клик на лого Яндекса и переход к новому окну")
    def click_on_yandex_logo_and_switch_to_new_window(self):
        self.click_element_and_switch_to_new_window(Header.YANDEX_LOGO)

    @allure.step("Проверяем что открыта главная страница Дзена")
    def dzen_main_page_is_displayed(self):
        return self.check_page_displayed(Header.DZEN_HEADER)

    @allure.step("Проверяем что открыта страница «Статус заказа»")
    def status_page_is_displayed(self):
        return self.check_page_displayed(Header.STATUS_ROADMAP)

