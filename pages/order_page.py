import allure

from pages.base_page import BasePage
from locators.order_page_locators import OrderPageLocators as Order
from data import BorderColor as Color
from assistant_methods import colors_match


class OrderPage(BasePage):
    @allure.step("Полное оформление заказа")
    def create_order(self, data):
        self.fill_all_fields(data)
        self.click_order_button()
        self.click_element(Order.ORDER_CHECK_WINDOW_YES_BUTTON)

    @allure.step("Проверяем что появилось окно «Заказ создан»")
    def order_created_popup_is_displayed(self):
        return self.check_page_displayed(Order.ORDER_CONFIRMED_WINDOW)

    @allure.step("Заполняем все поля в обеих формах")
    def fill_all_fields(self, data):
        self.who_orders_fill_fields(data)
        self.click_next_button()
        self.about_rent_fill_fields(data)

    @allure.step("Проверяем что открыта форма «Для кого самокат»")
    def who_orders_page_is_displayed(self):
        return self.check_page_displayed(Order.NEXT_BUTTON)

    @allure.step("Заполняем все поля формы «Для кого самокат»")
    def who_orders_fill_fields(self, data):
        self.fill_name_field(data["name"])
        self.fill_surname_field(data["surname"])
        self.fill_address_field(data["address"])
        if "station" in data:
            self.select_station(data["station"])
        self.fill_phone_field(data["phone"])

    @allure.step("Клик на кнопку «Далее» в форме «Для кого самокат»")
    def click_next_button(self):
        self.click_element(Order.NEXT_BUTTON)

    @allure.step("Клик на кнопку «Далее» + проверка, что открылась сл страница")
    def click_next_button_and_check_next_page_displayed(self):
        self.click_next_button()
        return self.check_page_displayed(Order.ORDER_BUTTON)

    @allure.step("Заполняем все поля формы «Про аренду»")
    def about_rent_fill_fields(self, data):
        self.fill_delivery_date(data["delivery_date"])
        if "rental_term" in data:
            self.select_rental_term(data["rental_term"])
        if "color" in data:
            self.select_colors(data["color"])
        if "comment" in data:
            self.fill_comment_field(data["comment"])
        self.random_click()

    @allure.step("Клик на кнопку «Заказать»")
    def click_order_button(self):
        self.click_element(Order.ORDER_BUTTON)

    @allure.step("Клик на кнопку «Заказать» + проверка, что открылось окно подтверждения")
    def click_order_button_and_check_confirmation_popup_displayed(self):
        self.click_element(Order.ORDER_BUTTON)
        return self.check_page_displayed(Order.ORDER_CHECK_WINDOW_YES_BUTTON)

    @allure.step("Клик на кнопку «Назад» на стр «Про аренду»")
    def click_back_button(self):
        self.click_element(Order.BACK_BUTTON)

    @allure.step("Заполняем поле «Имя»")
    def fill_name_field(self, name):
        self.fill_field(Order.NAME_INPUT, name)
        self.random_click()

    @allure.step("Заполняем поле «Фамилия»")
    def fill_surname_field(self, surname):
        self.fill_field(Order.SURNAME_INPUT, surname)
        self.random_click()

    @allure.step("Заполняем поле «Адрес»")
    def fill_address_field(self, address):
        self.fill_field(Order.ADDRESS_INPUT, address)
        self.random_click()

    @allure.step("Выбираем станцию в выпад. списке")
    def select_station(self, station_name):
        station_locator = self.create_locator(Order.STATION_TEMPLATE, station_name)
        self.click_element(Order.STATION_SELECT_BOX)
        self.scroll_to_element(station_locator)
        self.click_element(station_locator)

    @allure.step("Заполняем поле «Станция метро» вручную")
    def fill_station_field_manually(self, station_name):
        self.fill_field(Order.STATION_SELECT_BOX, station_name)

    @allure.step("Возвращаем текущее значение поля «Станция метро»")
    def return_station_field_value(self):
        self.random_click()
        return self.get_value(Order.STATION_SELECT_BOX)

    @allure.step("Заполняем поле «Телефон»")
    def fill_phone_field(self, phone):
        self.fill_field(Order.PHONE_INPUT, phone)
        self.random_click()

    @allure.step("Заполняем поле «Дата доставки»")
    def fill_delivery_date(self, delivery_date):
        self.fill_field(Order.DELIVERY_DATE_PICKER, delivery_date)
        self.random_click()

    @allure.step("Выбираем срок аренды в выпад. списке")
    def select_rental_term(self, amount_of_days):
        rental_term = self.create_locator(Order.RENTAL_TERM_TEMPLATE, amount_of_days)
        self.click_element(Order.RENTAL_TERM_SELECT_BOX)
        self.scroll_to_element(rental_term)
        self.click_element(rental_term)

    @allure.step("Возвращаем текущее значение поля «Срок аренды»")
    def return_rental_term_select_box_value(self):
        return self.get_text(Order.RENTAL_TERM_SELECT_BOX)

    @allure.step("Выбираем цвет (чекбоксы)")
    def select_colors(self, colors):
        if isinstance(colors, str):
            colors = [colors]
        for color in colors:
            color_checkbox = self.create_locator(Order.COLOR_CHECKBOX_TEMPLATE, color)
            if self.check_element_displayed(color_checkbox):
                self.click_element(color_checkbox)

    @allure.step("Заполняем поле «Комментарий»")
    def fill_comment_field(self, comment):
        self.fill_field(Order.COMMENT_INPUT, comment)

    def return_who_orders_fields_values(self):
        result = {}
        result['name'] = self.get_value(Order.NAME_INPUT)
        result['surname'] = self.get_value(Order.SURNAME_INPUT)
        result['address'] = self.get_value(Order.ADDRESS_INPUT)
        result['station'] = self.get_value(Order.STATION_SELECT_BOX)
        result['phone'] = self.get_value(Order.PHONE_INPUT)
        return result

    @allure.step("Проверяем, какая подсветка у поля (красная/чёрная) и выводится ли сообщение о некорректном вводе")
    def check_highlight_and_error_message(self, field_locator, error_message_sample):
        result = "Smth wrong"
        highlight = self.check_highlight(field_locator)
        error_message = self.check_error_message(error_message_sample)
        if highlight == "Black" and error_message is None:
            result = "Black highlight, no error message"
        if error_message and highlight == "Red":
            result = "Red highlight and error message"
        return result

    @allure.step("Проверяем, какая подсветка у поля")
    def check_highlight(self, field_locator):
        result = "smth wrong"
        border_color = self.get_border_color(field_locator)
        if colors_match(border_color, Color.BLACK):
            result = "Black"
        if colors_match(border_color, Color.ERROR_RED):
            result = "Red"
        return result

    @allure.step("Проверяем, выводится ли сообщение о некорректном вводе")
    def check_error_message(self, error_message_sample):
        error_message_locator = self.create_locator(Order.ERROR_MESSAGE_TEMPLATE, error_message_sample)
        if self.check_element_displayed(error_message_locator):
            return True

