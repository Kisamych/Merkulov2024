my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5] # Исходный список

positive_number = 0 # положительное число

while positive_number < len(my_list):  # создаем цикл

    if my_list[positive_number] < 0: # если число меньше нуля из списка, исключаем
        break

    if my_list[positive_number] > 0: # Если число больше нуля из списка, то выводим на экран
        print(my_list[positive_number])

    positive_number += 1 # формула += 1 нужна, чтоб цикл не длился бесконечно, а шел по списку и был закольцован (формула получается а=а+1)