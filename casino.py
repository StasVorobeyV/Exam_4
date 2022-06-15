#Казино.
#Компьютер генерирует числа от 1 до 10 и от 1 до 2-х соответственно.
#Цифры от одного до 10 отвечают за номера, а от 1 до 2 за цвета(1-красный,2 черный).
#Пользователю дается 5 попыток угадать номер и цвет
#(Прим. введения с  клавиатуры: 3 красный).
#В случае неудачи вывести на экран правильную комбинацию.


from random import random


a = round(random() * 10)
b = 1
print("computer riddle  number. what is number. 10 attempts: ")
while b <= 10:
    x = int(input(str(b) + " - attempts: "))
    if x > a :
        print("much")
    elif x < a:
        print("few")
    else:
        print("Yes, this is True number, bingo, we winner with %d - attempt" %b)
        break
    b += 1
else:
    print("bye bye... sorry, you have no attempts left, guessed nunber", a)