### 3. Напишите программу, которая принимает на вход координаты точки (X и Y), 
# причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости, 
# в которой находится эта точка (или на какой оси она находится).

# *Пример:*
# - x=34; y=-30 -> 4
# - x=2; y=4-> 1
# - x=-34; y=-30 -> 3

x = int(input('Input coordinate x: ')) # тип запрашиваемых данных для х и у мог быть также и float. Я здесь ориентируюсь на пример
y = int(input('Input coordinate y: '))
if x > 0 and y > 0:
    print('Your point is in the I quarter')
elif x < 0 and y > 0:
    print('Your point is in the II quarter')
elif x < 0 and y < 0:
    print('Your point is in the III quarter')
elif x > 0 and y < 0:
    print('Your point is in the IV quarter')
elif x == 0 and y !=0:
    print('Your point is lying on the Y-axis')
elif y == 0 and x !=0:
    print('Your point is lying on the X-axis')
else:
    print('x and y coordinates cannot be = 0 in the same time. Try again')
