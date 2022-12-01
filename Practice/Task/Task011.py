# Дано число из отрезка [10, 99]. Показать наибольшую цифру числа

import random
number = random.randint (10 , 99)


print (number)

def num (max):              # Надо разобраться!!!!
    numMax = number % 10 
    numMin = number // 10
    max = 0
    if numMax > numMin:
        max = numMax
    else:
        max = numMin
    return f'{max}, Число'
      


print (number)
print (num (max))

