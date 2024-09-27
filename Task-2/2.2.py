number = input("Введите число: ")

if len(number) == 4:
    print("Цифра в тысячах =", number[0])
    print("Цифра в сотнях =", number[1])
    print("Цифра в десятках =", number[2])
    print("Цифра в единицах =", number[3])
else:
    print("Ошибка: введите четырёхзначное число.")
