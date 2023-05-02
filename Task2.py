from random import randint

minny = int(input('Укажите минимальное число, которое может использоваться для генерации списка: '))
maxxy = int(input('Укажите максимальное число, которое может использоваться для генерации списка: '))
print(list_n := [randint(minny, maxxy) for _ in range(int(input('Сколько чисел в списке? ')))])
range_min = int(input('Значение нижней границы диапазона поиска: '))
range_max = int(input('Значение верхней границы диапазона поиска: '))
list_indexes = list()
for i in range(len(list_n)):
    if list_n[i] >= range_min and list_n[i] <= range_max:
        list_indexes.append(i)
print('Вывожу перечень индексов: ', list_indexes)
