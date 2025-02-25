from selenium.webdriver import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.common.exceptions import NoSuchElementException


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def wait_for_element(self, locator):
        WebDriverWait(self.driver, 3).until(
            expected_conditions.visibility_of_element_located(locator))

    def return_element(self, locator):
        self.wait_for_element(locator)
        return self.driver.find_element(*locator)

    def check_element_displayed(self, locator):
        try:
            element = self.driver.find_element(*locator)
            return element.is_displayed()
        except NoSuchElementException:
            return False

    def check_page_displayed(self, page_locator):
        if self.check_element_displayed(page_locator):
            return "displayed"
        else:
            return "not displayed"

    def scroll_to_element(self, locator):
        element = self.return_element(locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
        WebDriverWait(self.driver, 5).until(
            expected_conditions.element_to_be_clickable(locator))

    def get_text(self, locator):
        element = self.return_element(locator)
        return element.text

    def get_value(self, locator):
        element = self.return_element(locator)
        return element.get_attribute('value')

    def fill_field(self, locator, text):
        element = self.return_element(locator)
        element.send_keys(text)

    def click_element(self, locator):
        element = self.return_element(locator)
        element.click()

    def click_element_and_switch_to_new_window(self, locator):
        self.click_element(locator)
        new_window = self.driver.window_handles[1]
        self.driver.switch_to.window(new_window)

    @staticmethod
    def create_locator(locator_template, index):
        method, locator = locator_template
        locator = locator.format(index)
        result = (method, locator)
        return result

    def action(self):
        return ActionChains(self.driver)

    def random_click(self):
        self.action().move_by_offset(250, 0).click().pause(1).perform()

    def pause(self):
        self.action().pause(2).perform()

    def get_border_color(self, field_locator):
        field = self.return_element(field_locator)
        border = self.driver.execute_script(
            "return window.getComputedStyle(arguments[0]).border;", field)
        return border
