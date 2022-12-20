# quarter = input()

# match quarter:
#     case "1":
#         print("x > 0, y > 0")
#     case "2":
#         print("x < 0, y > 0")
#     case "3":
#         print("x < 0, y < 0")
#     case "4":
#         print("x > 0, y < 0")
#     case _:
#         print("error")

# 1. Напишите программу, которая принимает на вход 
# число N и выдаёт последовательность из N членов.
# 1, -3, 9, -27, 81


# n = int(input())

# for i in range(n):
#     print((-3) ** i, end = ' ')

# n = int(input())
# seq_n = 1

# for i in range(n):
#     print(seq_n, end = ' ')
#     seq_n*=-3
    
# 2. Создать список, длины n, значения формируются 
# по формуле 3k + 1,
#    где k принимает значения от 1 до n включительно.

# num_list = []
# n = int(input('Input a number: '))
# for k in range(1, n+1):
#     num_list.append(3*k + 1) 
# print(num_list)

# 3. Напишите программу, в которой пользователь 
# будет задавать две строки,
#    программа - определять количество 
# вхождений одной строки в другой.

n = input()
m = input()

print(n.count(m))
