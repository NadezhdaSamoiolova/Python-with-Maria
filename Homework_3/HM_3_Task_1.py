# 1. Задайте список, состоящий из произвольных чисел, количество задаёт пользователь.
# Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётных позициях(не индексах).
# in
# 5
# out
# [10, 2, 3, 8, 9]
# 22

# in
# 4
# out
# [4, 2, 4, 9]
# 8

# import numpy as np   ##### это я нашла в интернете, как можно создать список со случайными элементами. Далее подправляю этот способ

# lst = np.random.randint(-10, 10, 5)
# print(lst)

def find_sum(your_list):
    sum_dig = 0
    for i in range(0, len(your_list), 2):
        sum_dig += your_list[i]
    print("Your sum is: ", sum_dig)


import numpy as np

lst = list(np.random.randint(
                        int(input("Input min possible el in your list: ")), 
                        int(input("Input max possible el in your list: ")), 
                        int(input("Input number of digits in your list: "))
                        ))               
print("Your list is: ", lst)

find_sum(lst)
