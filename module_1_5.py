immutable_var = 1, 2, True, "ФИО"
print(immutable_var)
# immutable_var [0] = 7 # Мы не можем заменить элемент, не поддерживает обращение по объектам.
mutable_list = (["День", "Ночь", "Утро", "Вечер"])
mutable_list[0]= "Обед"
print(mutable_list)