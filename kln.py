# календарь

mec = int(input("Введите номер месяца : "))

if mec == 1 or mec == 2 or mec == 12 :
    print("зима")

elif mec == 3 or mec == 4 or mec == 5 :
    print("весна")

elif mec == 6 or mec == 7 or mec == 8 :
    print("лето")

elif mec == 9 or mec == 10 or mec == 11 :
    print("осень")

else:
    print("ошибка")