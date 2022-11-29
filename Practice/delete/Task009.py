# Найти длину отрезка заданного двумя точками: А(x1, y1) и B(x2, y2). 
# В прямоугольной декартовой системе координат.

import math

x1 = 1
x2 = 5
y1 = 1
y2 = 5

result1 = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
result13 = ((x2 - x1) ** 2 + (y2 - y1) ** 2)
result2 = math.sqrt (result13)

print (result2)
print (result1)