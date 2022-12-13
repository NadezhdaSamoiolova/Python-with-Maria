# 1. Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным.
# *Пример:*
# - 6 -> да
# - 7 -> да
# - 1 -> нет

num = int(input('Input a number from 1 to 7: '))
if 1 <= num <= 5:
    print('No. This is a weekday')
elif num == 6 or num == 7:
    print('Yes. This is a weekend')
else:
    print('You typed a wrong number. Try again')
