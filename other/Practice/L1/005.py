#2: Дана дата в формате dd.mm.yyyy, например: 02.11.2013. Ваша задача — вывести дату 
#в текстовом виде, например: второе ноября 2013 года. Склонением пренебречь (2000 года, 2010 года)

date = "02.07.2013"
d , m , y = date.split (".")

day = {
    "01" : "Первое" , 
    "02" : "Второе" , 
    "03" : "Третье" ,
    "04" : "Четвертое", 
    "05" : "Пятое", 
    "06" : "Шестое", 
    "07" : "Седьмое", 
    "08" : "Восьмое", 
    "09" : "Девятое", 
    "10" : "Десятое",
}
month = {
    "01" : "Январь",
    "02" : "Февраль",
    "03" : "Март",
    "04" : "Апрель",
    "05" : "Май",
    "06" : "Июнь",
    "07" : "Июль",
    "08" : "Август",
    "09" : "Сентябрь",
    "10" : "Октябрь",
    "11" : "Ноябрь",
    "12" : "Декабрь", 
} 

result = f" {day [d]} {month [m]} {y} года " 

#print(day)
#print (month)
print (result)