# 1. Задайте список, состоящий из произвольных чисел, 
# количество задаёт пользователь.
#    Напишите программу, которая определит, 
# присутствует ли в заданном списке число,
#    полученное от пользователя.
# from random import sample

# def find_number(amount, user_number):
#     new_list = sample(range(1, (amount+1) * 2), k=amount)
#     print(new_list)
#     if user_number in new_list:
#         return 'yes'
#     return 'no'

# some_number = find_number(int(input('Enter amount: ')), 
#                           int(input('Enter the desired number - ')))
# print(some_number)

# 2. Задайте список, состоящий из произвольных слов, 
# количество задаёт пользователь.
#    Напишите программу, которая определит индекс 
# второго вхождения строки в списке
#    либо сообщит, что её нет.

from random import sample

def words_list(num, word='abc'):
    w_list = []
    for i in range(num):
        m = sample(word, k=3)
        w_list.append(''.join(m))
    return w_list

def find_second(n_list, word):
    if word in n_list and n_list.count(word) > 1:
        c = n_list.index(word)
        print(n_list.index(word, c + 1))
    else: 
        print(-1)

n = int(input('Input a number: '))


u = words_list(n)
print(u)
w = input('Input a word: ')
find_second(u, w)

