def get_matrix(n, m, value):
    matrix = [] # создан пустой список
    for i in range(n): # первый(внешний) цикл for для кол-ва строк матрицы, n повторов.
        matrix.append([]) # пустой список в список matrix
        for j in range(m): # второй(внутренний) цикл for для кол-ва столбцов матрицы, m повторов.
            matrix[i].append(value) # пустой список значениями value.
    return matrix # Оператор return используется в функциях для возвращения данных после выполнения работы самой функции.

result1 = get_matrix(2, 2, 10)
result2 = get_matrix(3, 5, 42)
result3 = get_matrix(4, 2, 13)
print(result1)
print(result2)
print(result3)