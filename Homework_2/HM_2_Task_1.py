# 1. Напишите программу, которая принимает на вход
# вещественное число и показывает сумму его цифр.
# Без работы с методами строк.
# in -> out
# - 6782 -> 23
# - 0.67 -> 13
# - 198.45 -> 27

num = float(input('Input a real number: '))
m = len(str(num))
num_digit = int(num * 10 ** (m - 2))
# print(num_digit)

l_num_digit = map(int, str(num_digit))
# print(list(l_num_digit))
sum = 0
for i in l_num_digit:
    sum += i
print(sum)
