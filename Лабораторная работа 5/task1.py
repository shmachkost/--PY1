from pprint import pprint  # импортируем функцию pprint из модуля pprint

number = 15  # количество цифр для которых нужно создать словарь
number_list = [{'bin': bin(num), 'dec': num, 'hex': hex(num), 'oct': oct(num)} for num in range(number+1)]
# создаем список с помощью list comprehension, элементами которого являются словари,
# содержащие пары 'система счисления': число в ней
pprint(number_list)
