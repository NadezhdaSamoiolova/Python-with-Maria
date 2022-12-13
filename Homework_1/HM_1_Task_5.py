### 5. Напишите программу, которая принимает на вход координаты двух точек 
# и находит расстояние между ними в 2D пространстве.

xA = int(input('Input coordinate x of A: '))
yA = int(input('Input coordinate y of A: '))

xB = int(input('Input coordinate x of B: '))
yB = int(input('Input coordinate y of B: '))

# AB = √(xb - xa)2 + (yb - ya)2

AB = round((((xB - xA)**2 + (yB - yA)**2) ** 0.5), 3)
print(AB)
