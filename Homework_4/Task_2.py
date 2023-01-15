# 2. Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.
# Простые делители числа
# Простые делители числа онлайн

# in
# 54

# out
# [2, 3, 3, 3]

# in
# 9990

# out
# [2, 3, 3, 3, 5, 37]

# in
# 650

# out
# [2, 5, 5, 13]

def find_prime(num):
    fact_list = []
    a = 2
    while num > 1:
        if num % a == 0:
            fact_list.append(a)
            num /= a
        else:
            a +=1
    return fact_list


print(find_prime(int(input("Input a number: "))))
