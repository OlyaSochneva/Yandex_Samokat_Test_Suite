import pytest
import requests
import json

from selenium import webdriver

from data import URL

from assistant_methods import order_payload


@pytest.fixture(scope="function")
def chrome():
    options = webdriver.ChromeOptions()
    options.add_argument("--window-size=1920,1080")
    options.add_argument("--disable-web-security")
    options.add_argument("--disable-notifications")
    driver = webdriver.Chrome(options=options)
    driver.get("https://qa-scooter.praktikum-services.ru/")
    yield driver
    driver.quit()


@pytest.fixture(scope="function")
def firefox():
    options = webdriver.FirefoxOptions()
    options.add_argument("--width=1920")
    options.add_argument("--height=1080")
    driver = webdriver.Firefox(options=options)
    driver.get("https://qa-scooter.praktikum-services.ru/")
    yield driver
    driver.quit()


@pytest.fixture(scope="function")
def create_order_and_return_track():
    payload = json.dumps(order_payload())
    response = requests.post(URL.ORDER, data=payload)
    track = str((response.json())["track"])
    yield track
    requests.put(URL.CANCEL_ORDER, params={"track": track})
