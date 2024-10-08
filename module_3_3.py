# Задача "Распаковка"
# 1. Функция с параметрами по умолчанию:
# Создайте функцию print_params(a = 1, b = 'строка', c = True), которая принимает три параметра со значениями по умолчанию (например сейчас это: 1, 'строка', True).
# Функция должна выводить эти параметры.
# Вызовите функцию print_params с разным количеством аргументов, включая вызов без аргументов.

def print_params(a = 1, b = 'строка', c = True):
    print(a, b, c)
print_params(5, 'утро', False)   # Вызов функции с тремя аргументами
print_params(466, 'ночь')           # Вызов функции с двумя аргументами + 1 по умолчанию
print_params(b = 'день')                  # Вызов функции с одним аргументом + 2 по умолчанию
print_params()                            # Вызов функции без аргументов
# Проверьте, работают ли вызовы print_params(b = 25) print_params(c = [1,2,3])
print_params(b = 25)
print_params(c = [1, 2, 3])

# 2. Распаковка параметров:
# Создайте список values_list с тремя элементами разных типов.
# Создайте словарь values_dict с тремя ключами, соответствующими параметрам функции print_params, и значениями разных типов.
# Передайте values_list и values_dict в функцию print_params, используя распаковку параметров (* для списка и ** для словаря).
values_list = [9, 'обед', False]
values_dict = {'a': 500, 'b': 'ужин', 'c': True}
print_params(*values_list) # *
print_params(**values_dict) # **
# Одновременно передать values_list и values_dict в функцию print_params невозможно,не изменив количество элементов.

# 3. Распаковка + отдельные параметры:
values_list_2 = [54.32, 'Строка']
print_params(*values_list_2, 42)


# Важно!
# Не передавайте списки задавая по умолчанию пустой список или другой изменяемый тип данных!
# В таком случае, если этот список будет изменён внутри функции, то на следующий вызов функции он останется в том же состоянии.
# def a(my_list = [])) – это приводит к ошибкам!
# Можно передавать вот так(список создаётся локально, мы не влияем на его изменение вне функции)
# def append_to_list(item, list_my=None):
#  if list_my is None:
#   list_my = []
#  list_my.append(item)
# print(list_my)
