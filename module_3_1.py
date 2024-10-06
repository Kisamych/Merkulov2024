calls = 0
# Создаём функцию count_calls и изменять в ней значение переменной calls.
def count_calls ():
    global calls
    calls+=1
# Создаём функцию string_info с параметром string
def string_info (string):
    count_calls()
    return (len(string), string.upper(), string.lower())
# Создаём функцию is_contains с двумя параметрами string и list_to_search
def is_contains (string, list_to_search):
    count_calls()
    return string.upper() in [s.upper() for s in list_to_search]
# Вывод результата
print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN']))
print(is_contains('cycle', ['recycle', 'cyclic']))
print(calls)

# Что нужно знать прежде, чем работать с global
# Когда мы создаем переменную внутри функции, она по умолчанию является локальной.
# Когда мы определяем переменную вне функции, она по умолчанию является глобальной. В этом случае не нужно использовать ключевое слово global.
# Ключевое слово global нужно для получения доступа к глобальной переменной и изменения ее внутри функции, то есть внутри локальной области видимости.
# Использовать ключевое слово global вне функции бессмысленно.