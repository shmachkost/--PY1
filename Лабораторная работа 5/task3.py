from random import randint  # импортируем функцию randint из модуля random
amount = 15  # задаем размер списка
min_ = -10  # задаем диапазон значений
max_ = 10
def get_unique_list_numbers() -> list[int]:  # создаем функцию, которая возвращает список, заполненный случайными целыми уникальными числами
    list_numbers = []  # создаем список
    while True:  # создаем цикл, который будет выполняться, пока количество уникальных чисел не будет равно заданному размеру
        number = randint(min_, max_)  # создаем случайное число в заданном диапазоне
        if number not in list_numbers:  # если этого числа еще не было в списке, то добавляем его в список
            list_numbers.append(number)
        if len(list_numbers) == amount:
            break
    return list_numbers  # возвращаем полученный список

list_unique_numbers = get_unique_list_numbers()  # делаем из локальной переменной глобальную
print(list_unique_numbers)
print(len(list_unique_numbers) == len(set(list_unique_numbers)))
