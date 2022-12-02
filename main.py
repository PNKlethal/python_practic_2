#1 задание. Создать список и заполнить его элементами различных типов данных. Реализовать скрипт проверки типа данных каждого элемента. Использовать функцию type() для проверки типа. Элементы списка можно не запрашивать у пользователя, а указать явно, в программе
list = [1, 2, -30, 'string', True, 3.5]

def my_type(element):
    for element in range(len(list)):
        print(type(list[element]))
    return

my_type(list)

#2 задание. Для списка реализовать обмен значений соседних элементов, т.е. значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т.д. При нечетном количестве элементов последний сохранить на своем месте. Для заполнения списка элементов необходимо использовать функцию input()

element_count = int(input("Введите количество элементов списка "))
my_list = []
i = 0
element = 0
while i < element_count:
    my_list.append(input("Введите значение списка "))
    i += 1

for elem in range(int(len(my_list)/2)):
        my_list[element], my_list[element + 1] = my_list [element + 1], my_list[element]
        element += 2
print(my_list)

#3 задание. Пользователь вводит месяц в виде целого числа от 1 до 12. Сообщить к какому времени года относится месяц (зима, весна, лето, осень). Напишите решения через list и через dict

the_seasons_list = ['winter', 'spring', 'summer', 'autumn']
the_seasons_dict = {1 : 'winter', 2 : 'spring', 3 : 'summer', 4 : 'autumn'}
month = int(input("Введите месяц по номеру "))
if month ==12 or month == 1 or month == 2:
        print(the_seasons_dict.get(1))
elif month == 3 or month == 4 or month ==5:
    print(the_seasons_dict.get(2))
elif month == 6 or month == 7 or month == 8:
    print(the_seasons_dict.get(3))
elif month == 9 or month == 10 or month == 11:
    print(the_seasons_dict.get(4))
else:
        print("Такого месяца не существует")

#4 задание. Пользователь вводит строку из нескольких слов, разделённых пробелами. Вывести каждое слово с новой строки. Строки необходимо пронумеровать. Если в слово длинное, выводить только первые 10 букв в слове.

my_string = input("введите несколько слов, это может быть предложение ")
my_word = []
number = 1
for element in range(my_string.count(' ') + 1):
    my_word = my_string.split()
    if len(str(my_word)) <= 10:
        print(f" {number} {my_word [element]}")
        number += 1
    else:
        print(f" {number} {my_word [element] [0:10]}")
        number += 1

#5 задание. Реализовать структуру «Рейтинг», представляющую собой не возрастающий набор натуральных чисел. У пользователя необходимо запрашивать новый элемент рейтинга. Если в рейтинге существуют элементы с одинаковыми значениями, то новый элемент с тем же значением должен разместиться после них.

my_list = [7, 5, 3, 3, 2]
print(f"Рейтинг - {my_list}")
digit = int(input("Введите число (555 -> выход) "))
while digit != 555:
    for el in range(len(my_list)):
        if my_list[el] == digit:
            my_list.insert(el + 1, digit)
            break
        elif my_list[0] < digit:
            my_list.insert(0, digit)
        elif my_list[-1] > digit:
            my_list.append(digit)
        elif my_list[el] > digit and my_list[el + 1] < digit:
            my_list.insert(el + 1, digit)
    print(f"текущий список - {my_list}")
    digit = int(input("Введите число (555 -> выход) "))