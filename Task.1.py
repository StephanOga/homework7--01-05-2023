first = int(input('Введите значение первого элемента прогрессии: '))
difference = int(input('Введите разность: '))
size = int(input('Введите количество элементов списка: '))
list_numbers = [first] * size
for i in range(1, size):
    list_numbers[i] = list_numbers[i-1] + difference
print(list_numbers)