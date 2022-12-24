# * 4. Напишите программу, которая принимает на вход 2 числа.
# Получите значение N, для пустого списка, заполните числами в диапзоне [-N, N].
# Найдите произведение элементов на указанных позициях(не индексах).
# Enter the value of N: 5
# Position one: 1
# Position two: 2
# -> [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5]
# -> 20

# Enter the value of N: 4
# Position one: 20
# Position two: 22
# -> [-4, -3, -2, -1, 0, 1, 2, 3, 4]
# -> There are no values for these indexes!

from random import randrange

N = randrange(1, 10)
print('N = ', N) 

list = []
for i in range(-N, N+1):
    list.append(i)
print(list)

len_list = len(list)
print('Lenght of the list is: ', len_list)

a = int(input('Input number a less or equal to the lenght of the list: '))
b = int(input('Input number b less or equal to the lenght of the list: '))
# print(list[a-1])
# print(list[b-1])

if  a <= len(list) and b <= len(list):
    mult = list[a-1] * list[b-1]
    print('A multiplication of numbers on positions a and b is: ', mult)
else:
    print('You entered a wrong numbers a and/or b')
