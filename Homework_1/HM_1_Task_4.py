### 4. Напишите программу, которая по заданному номеру четверти, 
# показывает диапазон возможных координат точек в этой четверти (x и y).
# *Пример:*

# - 1 -> x > 0, y > 0
# - 8 -> нет такой четверти

num = int(input('Input number of the quarter from 1 to 4: '))
if num == 1:
    print('x > 0, y > 0')
elif num == 2:
    print('x < 0, y > 0')
elif num == 3:
    print('x < 0, y < 0')
elif num == 4:
    print('x > 0, y < 0')
else:
    print('You entered a wrong number. There are not a qurter with such number.')
