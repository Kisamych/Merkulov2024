def single_root_words(root_word, *other_words): # Объявите функцию single_root_words и напишите в ней параметры root_word и *other_words.
    same_words = [] # Создайте внутри функции пустой список same_words, который пополнится нужными словами.
    root_word_lower = root_word.lower()

    for word in other_words: # При помощи цикла for переберите предполагаемо подходящие слова.
        word_lower = word.lower()
        if root_word_lower in word_lower or word_lower in root_word_lower:
            same_words.append(word) # Пропишите корректное относительно задачи условие, при котором добавляются слова в результирующий список same_words.
    return same_words # После цикла верните образованный функцией список same_words.
# Вызовите функцию single_root_words и выведете на экран(консоль) возвращённое ей значение.
result1 = single_root_words('rich', 'richiest', 'orichalcum', 'cheers', 'richies')
result2 = single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel')

print(result1)
print(result2)
