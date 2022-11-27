import json

INPUT_FILE = "input.csv"

# Реализуем конвертер из csv в json формат
def csv_to_list_dict(filename, delimiter=',', new_line='\n') -> list[{dict}]:
    with open(filename) as f:
        table = []  # создаем список
        for index, line in enumerate(f):
            # разделяем строку на список подстрок по разделителю запятая и убираем конечный символ '\n'
            data_list = line.strip(new_line).split(delimiter)
            # Если мы на первой строке, сохраняем стоку как заголовки
            if index == 0:
                heads = data_list
                continue  # Возвращаемся в начало цикла FOR

            table.append({})  # Добавляем новый словарь в список

            for i, _ in enumerate(heads):
                # Берем последний элемент списка (добавленный словарь)
                # Добавляем в него нужный элемент
                table[-1][heads[i]] = data_list[i]  # причем i-ый заголовок это ключ, а i-ое число это значение
    return table  # функция возвращает список словарей

print(json.dumps(csv_to_list_dict(INPUT_FILE), indent=4))  # Распечатываем json строку с отступами равными 4.