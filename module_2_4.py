numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15] # список чисел
primes = [] #список primes содержащий только простые числа.
not_primes = [] #список not_primes, содержащий все не простые числа.
for i in numbers:  # переберает список numbers
    is_prime = True # перебирает список primes. True (истина) и False (ложь).
    if i == 1:
        continue # continue дает возможность пропустить часть цикла, где активируется внешнее условие, но при этом выполнить остальную часть цикла
    for j in range(2, i): #range возвращает последовательность чисел в заданном диапазоне с заданным шагом. Star|stop|step - начало, конец, шаг
        if i % j == 0:
            is_prime = False
            break #break позволяет прервать цикл при возникновении внешнего фактора
    if is_prime:
        primes.append(i) #  append () используется для добавления одного элемента в конец списка.
    else:
        not_primes.append(i)
print(primes)
print(not_primes)

#Цикл for может перебирать словари
# dict_ = {'a': 1, 'b':2, 'c':3}
#for i in dict_:
#   print(i, dict_[i])