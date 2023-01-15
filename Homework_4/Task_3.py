# 3. Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности в том же порядке.
# in
# 7

# out
# [4, 5, 3, 3, 4, 1, 2]
# [5, 1, 2]

# in
# -1

# out
# Negative value of the number of numbers!
# []

# in
# 10

# out
# [4, 4, 5, 5, 6, 2, 3, 0, 9, 4]
# [6, 2, 3, 0, 9]

import numpy as np

# a = int(input("Input a number: "))
# lst = list(np.random.randint(1, 10, a))
# print(lst)

# end_lst = []
# for i in lst:
#     if lst.count(i) == 1:
#         end_lst.append(i)
# print(end_lst)

def find_only_el(lst):
    end_lst = []
    for i in lst:
        if lst.count(i) == 1:
            end_lst.append(i)
    return end_lst


a = int(input("Input a number: "))
lst = list(np.random.randint(1, 10, a))
print(lst)

print(find_only_el(lst))

##### Решение Марии - с использованием словарей ####

# def uniq_el(list_nums: list):
#     result = []
#     my_dict = {}.fromkeys(list_nums, 0) # словарь создастся со значениями ключей в ед. экземпляре. Т.е. если в списке было две пятерки, будет один эл-т словаря с ключом 5

#     for i in list_nums:
#         my_dict[i] += 1 # проходимся по исходному списку, как по ключам и каждому значению в словаре прибавим 1. Если в списке было 2 пятерки, в словаре к значениям добавится два раза по 1 

#     for k in my_dict:
#         if my_dict[k] == 1:
#             result.append(k) # проходимся по значениям в полученном словаре. Если значение = 1 - забираем ключ в итоговоый список
#     return result

