from selenium.webdriver.common.by import By


class OrderPageLocators:
    # локаторы полей ввода:
    NAME_INPUT = By.XPATH, '// input[@placeholder="* Имя"]'
    SURNAME_INPUT = By.XPATH, '// input[@placeholder="* Фамилия"]'
    ADDRESS_INPUT = By.XPATH, '// input[@placeholder="* Адрес: куда привезти заказ"]'
    STATION_SELECT_BOX = By.XPATH, '// input[@placeholder="* Станция метро"]'
    PHONE_INPUT = By.XPATH, '// input[@placeholder="* Телефон: на него позвонит курьер"]'
    DELIVERY_DATE_PICKER = By.XPATH, '// input[@placeholder="* Когда привезти самокат"]'
    RENTAL_TERM_SELECT_BOX = By.XPATH, '// div[contains(@class, "Dropdown-root")]'
    COMMENT_INPUT = By.XPATH, '// input[@placeholder="Комментарий для курьера"]'

    # шаблон локатора станции:
    STATION_TEMPLATE = By.XPATH, '// div[text()="{}"]/parent::button'

    # шаблон локатора для пунктов выпадающего списка «Срок аренды»:
    RENTAL_TERM_TEMPLATE = By.XPATH, '// div[@role="option" and text()="{}"]'

    # шаблон локатора чекбокса для выбора цвета:
    COLOR_CHECKBOX_TEMPLATE = By.XPATH, '// label[text()="{}"]/child::input[@type="checkbox"]'

    # шаблон локатора для сообщений о некорректном вводе:
    ERROR_MESSAGE_TEMPLATE = By.XPATH, '// div[text()="{}"]'

    # шаблон локатора для сообщений об ошибке через локатор поля:
    ERROR_TEMPLATE = By.XPATH, '{}/following-sibling::div[contains(@class, "Error")]'

    # кнопка «Далее» на стр «Для кого самокат»:
    NEXT_BUTTON = By.XPATH, '//button[text()="Далее"]'

    # Кнопка «Назад» на стр «Про аренду»:
    BACK_BUTTON = By.XPATH, '// button[text()="Назад"]'

    # Кнопка «Заказать» на стр «Про аренду»:
    ORDER_BUTTON = By.XPATH, '// div[contains(@class, "Order_Buttons")]/child::button[text()="Заказать"]'

    # Кнопка «Да» в окне подтверждения заказа:
    ORDER_CHECK_WINDOW_YES_BUTTON = By.XPATH, '//button[text()="Да"]'

    # Окно «Заказ оформлен»:
    ORDER_CONFIRMED_WINDOW = By.XPATH, '// div[text()="Заказ оформлен"]'


