import random
import string
from datetime import timedelta, datetime


def colors_match(actual_rgb, expected_hex):
    expected_rgb = str(hex_to_rgb(expected_hex))
    if expected_rgb in actual_rgb:
        return True


def hex_to_rgb(hex_color):
    hex_color = hex_color.lstrip('#')
    return tuple(int(hex_color[i:i + 2], 16) for i in (0, 2, 4))


def add_days_to_current(number_of_days):
    current_date = datetime.now().date()
    delivery_date = current_date + timedelta(days=number_of_days)
    result = delivery_date.strftime('%d.%m.%Y')
    return result


def order_payload():  # без указания цвета
    payload = {
        "firstName": generate_random_string(5),
        "lastName": generate_random_string(5),
        "address": generate_random_string(5),
        "metroStation": choose_random_station(),
        "phone": generate_phone_number(),
        "rentTime": choose_random_rent_time(),
        "deliveryDate": add_days_to_current(2),
    }
    return payload


def generate_random_string(length):
    letters = string.ascii_lowercase
    random_string = ''.join(random.choice(letters) for i in range(length))
    return random_string


def choose_random_station():
    return random.randint(1, 237)  # т.к. всего станций в списке Самоката 237


def generate_phone_number():
    phone_number = '89'
    for i in range(9):
        phone_number += random.choice(string.digits)
    return phone_number


def choose_random_rent_time():
    return random.randint(1, 7)
