money = int(input('Money: '))
while money // 8 > 0:
    money //= 8
print(money)