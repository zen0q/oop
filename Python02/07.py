a = float(input("Введите число: "))
if (a < 10 ** -6) or a == 0:
    print(1000000)
else:
    print(a ** -1)