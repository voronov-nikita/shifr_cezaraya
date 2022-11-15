# Шифр Цезаря - простое перемещение всех букв алфавита на одно и тоже значение
# Это очень хорошая тернировка для начинающего програмиста.
# В данном алгоритме не будет задействовано изменение цифр и символов, что упрощает его создание.

# Для случайного значения числа перемешивания применим модуль random
# А для большей скорости програмы импортируем всего одну функцию - randint
from random import randint


# Гораздо удобнее, если брать функцию, а уже потом подстовлять туда списки
# Это сокращает время написания кода и делает его более читабельным.
def peremeshivanie(listt):
    # Сместим все значения на случайное число r
    r = randint(1, 10)
    ind = 0
    for elem in listt:
        listt[listt.index(elem)] = listt[listt.index(ind + r)]
        ind += 1
    return listt


# Списки, в которых будят храниться все буквы английского и русского алфавита
ls_en_min = []
ls_ru_min = []
ls_ru_max = []
ls_en_max = []

# Заполним списки с помощью функций chr() и ord()
for i in range(ord("A"), ord("Z") + 1): ls_en_max.append(chr(i))
for i in range(ord("a"), ord("z") + 1): ls_en_max.append(chr(i))
for i in range(ord("А"), ord("Я") + 1): ls_en_max.append(chr(i))
for i in range(ord("а"), ord("я") + 1): ls_en_max.append(chr(i))

print(peremeshivanie(ls_en_min))
