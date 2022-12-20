# ** 5. Реализуйте алгоритм перемешивания списка.
# Без функции shuffle из модуля random.
# 10
# -> [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# -> [0, 7, 6, 3, 4, 2, 9, 5, 1, 8]

from random import randrange

N = randrange(1, 10)
print('N = ', N) 

list = []
for i in range(N):
    list.append(i)
print('List is: ', list)

list_1 = []
for i in list:
    list_1.append((randrange(N)))
print('List_1 is: ' , list_1)

