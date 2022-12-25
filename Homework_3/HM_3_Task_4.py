# * 4. Задайте список из произвольных вещественных чисел, количество задаёт пользователь.
# Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
# in
# 5
# out
# [5.16, 8.62, 6.57, 7.92, 9.22]
# Min: 0.16, Max: 0.92. Difference: 0.76

# in
# 3
# out
# [9.26, 8.5, 1.14]
# Min: 0.14, Max: 0.5. Difference: 0.36

# a = 888.987 % 1
# b = round(a, 3)
# print(b)

# lst_1 = [5.16, 8.62, 6.57, 7.92, 9.22]

def find_dif(lst_1):
    lst_neu = []
    for i in range(len(lst_1)):
        a = round(lst_1[i] % 1, 2) 
        lst_neu.append(a)
    print('Min: ', min(lst_neu), 'Max: ', max(lst_neu), 'Difference: ', round(max(lst_neu) - min(lst_neu), 2))

from random import uniform

def create_list(a, b, c):
    lst = []
    for i in range(c):
        x = round(uniform(a, b), 2)
        lst.append(x)
    return lst
    # print(lst)


a = int(input('Input a min digit in your list: '))
b = int(input('Input a max digit in your list: '))
c = int(input('Input a number of elements in your list: '))

lst = create_list(a, b, c)
print(lst)
# lst_str = str(lst)
# lst_list = list(lst_str)

# print(type(lst_list))
find_dif(lst)
