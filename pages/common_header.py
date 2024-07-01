from pages.base_page import BasePage
from locators.common_header_locators import CommonHeaderLocators as Header


class CommonHeader(BasePage):
    def click_on_order_button(self):
        self.click_element(Header.HEADER_ORDER_BUTTON)

    def return_to_main_page_by_click_on_logo(self):
        self.click_element(Header.SCOOTER_LOGO)

    def click_on_order_status_button(self):
        self.click_element(Header.ORDER_STATUS_BUTTON)

    def find_order(self, order_number):
        self.click_on_order_status_button()
        self.fill_field(Header.SEARCH_ORDER_INPUT, order_number)
        self.click_element(Header.GO_BUTTON)
        self.pause()

    def click_on_yandex_logo_and_switch_to_new_window(self):
        self.click_element_and_switch_to_new_window(Header.YANDEX_LOGO)

    def dzen_main_page_is_displayed(self):
        return self.check_page_displayed(Header.DZEN_HEADER)

    def status_page_is_displayed(self):
        return self.check_page_displayed(Header.STATUS_ROADMAP)

