# 3. Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# Без использования встроенной функции преобразования, без строк.
# in
# 88
# out
# 1011000

# in
# 11
# out
# 1011

def make_binary(num):
    if num > 0:
        lst = []
        while num >= 2:
            my_num = int(num % 2)
            num = num / 2
            lst.append(my_num)
        lst.append(1)
        lst.reverse()
        print('Your binary num is: ', *lst, sep="")
    
    else:
        print("You entered a wrong number. Try again")
       
       
a = int(input('Input a number > 0: '))
make_binary(a)
       