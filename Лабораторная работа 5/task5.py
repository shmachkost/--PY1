import random  # импортируем модуль random
import string  # импортируем модуль string
def get_random_password(n=8) -> str:  # создаем функцию для генерации случайных паролей заданной длины n (по умолчанию 8 символов)
    up_letters = string.ascii_uppercase  # создаем строку, состоящую из английских букв верхнего регистра: A - Z
    low_letters = string.ascii_lowercase  # создаем строку, состоящую из английских букв нижнего регистра: a - z
    digits = string.digits  # создаем строку, состоящую из цифр: 0 - 9
    combined_string = up_letters + low_letters + digits  # создаем строку, состоящую из предыдущих 3 строк
    password_list = random.sample(combined_string, n)  # создаем список, состоящий из n случайных символов
    password = "".join(password_list)  # преобразуем список в строку-пароль
    return password  # возвращаем полученный пароль

print(get_random_password())