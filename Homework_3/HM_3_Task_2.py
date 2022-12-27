# 2. Напишите программу, которая найдёт произведение пар чисел списка.
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# in
# 4
# out
# [2, 5, 8, 10]
# [20, 40]

# in
# 5
# out
# [2, 2, 4, 8, 8]
# [16, 16, 4]

def find_mult(lst):
    new_list = []
    i = 0
    if len(lst) % 2 == 0:
        while i < ((len(lst)) / 2):
            new_list.append(lst[i] * lst[(-1)*(i+1)])
            i += 1
        print(new_list)
    
    elif len(lst) % 2 != 0:
        while i < ((len(lst)-1) / 2):
            new_list.append(lst[i] * lst[(-1)*(i+1)])
            i += 1
        new_list.append(lst[int(((len(lst)-1) / 2))])
        print(new_list)


import numpy as np

your_list = list(np.random.randint(
                        int(input("Input min possible el in your list: ")), 
                        int(input("Input max possible el in your list: ")), 
                        int(input("Input number of digits in your list: "))
                        ))               
print("Your list is: ", your_list)

find_mult(your_list)
