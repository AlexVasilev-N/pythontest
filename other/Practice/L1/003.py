#3: Создайте программу “Медицинская анкета”, 
# где вы запросите у пользователя следующие данные: имя, фамилия, возраст и вес.
#Пациент в хорошем состоянии, если ему до 30 лет и вес от 50 и до 120 кг,
##Пациенту требуется заняться собой, если ему более 30 и вес меньше 50 или больше 120 кг
#Пациенту требуется врачебный осмотр, если ему более 40 и вес менее 50 или больше 120 кг.


name = input ("Ваше имя: ")
sname = input ("Ваша фамиля: ")
age = int (input ("Ваш возраст: "))
weight = int (input ( "Ваш вес: "))

if age < 30 and 50 < weight <  120:
    print ("Пациент в хорошем состоянии")

elif 30 <= age <=40 and 50 > weight > 120:
    print ("Пациенту требуется заняться собой")

elif age > 40 and 50 > weight > 120: 
    print ("Пациенту требуется врачебный осмотр")

else:
    print ("У Вас все хорошо")

