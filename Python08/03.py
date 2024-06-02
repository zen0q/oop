symbol = ('_', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0')

name = list(input())

for i in name:
    if i != i.upper() or i in symbol:
      pass

    else:
        print("Неверный символ:", i)
        break
else:
    print("OK")