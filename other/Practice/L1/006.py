#3: Дан список заполненный произвольными целыми числами.
#Получите новый список, элементами которого будут только уникальные элементы исходного.
#    Примечание. Списки создайте вручную, например так:
#my_list_1 = [2, 2, 5, 12, 8, 2, 12]

#В этом случае ответ будет:
#[5, 8]

numbers = [2, 2, 5, 12, 8, 2, 12, 43, 13, 25]

result = []

for number in numbers:
    if numbers.count (number) == 1:
        result.append(number)

print (result)
