from selenium.webdriver.common.by import By


class MainPageLocators:
    # Кнопка «Заказать» внутри главной страницы:
    ORDER_BUTTON = By.XPATH, '// div[contains(@class, "FinishButton")]/child::button'

    # шаблон локатора для вопросов:
    QUESTION_TEMPLATE = By.ID, 'accordion__heading-{}'

    # шаблон локатора для ответов:
    ANSWER_TEMPLATE = By.ID, 'accordion__panel-{}'

