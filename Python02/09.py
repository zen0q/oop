Borya = int(input("Введите рост Бори: "))
Vova = int(input("Введите рост Вовы: "))
Dima = int(input("Введите рост Димы: "))
if (Borya > Vova) and (Borya > Dima) and (Vova > Dima):
    print(Borya, Vova, Dima)
elif (Borya > Vova) and (Borya > Dima) and (Vova < Dima):
    print(Borya, Dima, Vova)
elif (Vova > Borya) and (Vova > Dima) and (Borya > Dima):
    print(Vova, Borya, Dima)
elif (Vova > Borya) and (Vova > Dima) and (Borya < Dima):
    print(Vova, Dima, Borya)
elif (Dima > Borya) and (Dima > Vova) and (Vova > Borya):
    print(Dima, Vova, Borya)
elif (Dima > Borya) and (Dima > Vova) and (Vova < Borya):
    print(Dima, Borya, Vova)
else:
    print("error")



