# ** 5. Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
# Негафибоначчи
# in
# 8
# out
# -21 13 -8 5 -3 2 -1 1 0 1 1 2 3 5 8 13 21

# in
# 5
# out
# 5 -3 2 -1 1 0 1 1 2 3 5

def fib(n):
    if n in [1, 2]:
        return 1
    else:
        return fib(n-1) + fib(n-2)

def negafib(n):
    # n_1 = n * (-1)
    if n == (-1):
        return 1
    elif n == (-2):
        return -1
    else: 
        return negafib(n + 2) - negafib(n + 1)


n = int(input('Input a int number: '))
list = []
for e in range(-n, 0):
    list.append(negafib(e))

list.append(0)

for e in range(1, n+1):
    list.append(fib(e))

print(*list, sep=' ')
