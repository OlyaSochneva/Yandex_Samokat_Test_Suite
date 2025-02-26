import allure

from assistant_methods import colors_match
from pages.base_page import BasePage
from locators.order_page_locators import OrderPageLocators as Order
from data import BorderColor as Color


class OrderPage(BasePage):
    @allure.step("Полное оформление заказа")
    def create_order_full_flow(self, data):
        self.fill_all_fields_and_order(data)
        self.click_element(Order.ORDER_CONFIRM_POPUP_YES_BUTTON)

    @allure.step("Проверяем, что появилось окно «Заказ оформлен»")
    def check_order_created_popup_displayed(self):
        return self.check_page_displayed(Order.ORDER_CREATED_POPUP)

    @allure.step("Заполняем обе формы + нажимаем «Заказать»")
    def fill_all_fields_and_order(self, data):
        self.first_order_page_fill_fields_and_next(data)
        self.second_order_page_fill_fields(data)
        self.click_order_button()

    @allure.step("Заполняем все поля в обеих формах")
    def fill_all_fields(self, data):
        self.first_order_page_fill_fields_and_next(data)
        self.second_order_page_fill_fields(data)

    @allure.step("Клик на кнопку «Заказать»")
    def click_order_button(self):
        self.click_element(Order.ORDER_BUTTON)

    @allure.step("Проверяем, что открылось окно подтверждения")
    def check_confirmation_popup_displayed(self):
        return self.check_page_displayed(Order.ORDER_CONFIRM_POPUP_YES_BUTTON)

    @allure.step("Заполняем форму «Для кого самокат» + нажимаем «Далее»")
    def first_order_page_fill_fields_and_next(self, data):
        self.first_order_page_fill_fields(data)
        self.click_next_button()

    @allure.step("Клик на кнопку «Далее» в форме «Для кого самокат»")
    def click_next_button(self):
        self.click_element(Order.NEXT_BUTTON)

    @allure.step("Проверка, что открылась сл страница")
    def is_second_order_page_displayed(self):
        return self.check_page_displayed(Order.ORDER_BUTTON)

    @allure.step("Заполняем все поля формы «Для кого самокат»")
    def first_order_page_fill_fields(self, data):
        self.fill_name_field(data["name"])
        self.fill_surname_field(data["surname"])
        self.fill_address_field(data["address"])
        if "station" in data:
            self.select_station(data["station"])
        self.fill_phone_field(data["phone"])

    @allure.step("Заполняем все поля формы «Про аренду»")
    def second_order_page_fill_fields(self, data):
        self.fill_delivery_date(data["delivery_date"])
        if "rental_term" in data:
            self.select_rental_term(data["rental_term"])
        if "color" in data:
            self.select_colors(data["color"])
        if "comment" in data:
            self.fill_comment_field(data["comment"])

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
        self.random_click()

    @allure.step("Возвращаем текущее значение поля «Станция метро»")
    def return_station_field_value(self):
        return self.get_value(Order.STATION_SELECT_BOX)

    @allure.step("Заполняем поле «Телефон»")
    def fill_phone_field(self, phone):
        self.fill_field(Order.PHONE_INPUT, phone)
        self.random_click()

    @allure.step("Заполняем поле «Дата доставки»")
    def fill_delivery_date(self, delivery_date):
        self.fill_field(Order.DELIVERY_DATE_PICKER, delivery_date)
        self.random_click()

    @allure.step("Возвращаем текущее значение поля «Дата доставки»")
    def return_delivery_date_picker_value(self):
        return self.get_value(Order.DELIVERY_DATE_PICKER)

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
        self.random_click()

    @allure.step("Проверяем, подсвечивается ли поле красным")
    def check_red_highlight(self, field_locator):
        if not self.check_element_displayed(field_locator):
            return "field not displayed"
        border_color = self.get_border_color(field_locator)
        if colors_match(border_color, Color.ERROR_RED):
            return "Red"
        return "No red highlight"

    @allure.step("Проверяем, выводится ли сообщение о некорректном вводе")
    def check_error_message(self, field_locator):
        if not self.check_element_displayed(field_locator):
            return "field not displayed"
        method, locator = field_locator
        error_message_locator = self.create_locator(Order.ERROR_TEMPLATE, locator)
        if self.check_element_displayed(error_message_locator):
            return self.get_text(error_message_locator)
        return "no error message"
