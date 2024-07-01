from selenium.webdriver.common.by import By


class CommonHeaderLocators:
    # Кнопка «Заказать» в хэдере:
    HEADER_ORDER_BUTTON = By.XPATH, '// div[contains(@class, "Header")]/child::button[text()="Заказать"]'

    # Кнопка «Статус заказа» в хэдере:
    ORDER_STATUS_BUTTON = By.XPATH, '// button[text()="Статус заказа"]'

    # Поле ввода для поиска заказа по номеру:
    SEARCH_ORDER_INPUT = By.XPATH, '// input[@placeholder="Введите номер заказа"]'

    # Кнопка «Go!» для поиска заказа
    GO_BUTTON = By.XPATH, '// button[text()="Go!"]'

    # лого Яндекса:
    YANDEX_LOGO = By.XPATH, '// *[@href="//yandex.ru"]'

    # лого Самоката:
    SCOOTER_LOGO = By.XPATH, '// *[contains(@class, "LogoScooter")]'

    # Шапка главной стр Дзена:
    DZEN_HEADER = By.XPATH, '// header[@id="dzen-header"]'

    # Цепочка статусов на стр «Статус заказа»:
    STATUS_ROADMAP = By.XPATH, '// div[contains(@class, "OrderRoadmap")]'

