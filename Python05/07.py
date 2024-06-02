n = int(input("Введите кол-во команд правительства: "))
a = 'Остазия'
b = 'Евразия'
for i in range(n):
    c = input()
    if c == 'С кем война?':
        print(b)
    if c == 'С кем мир?':
        print(a)
    if c == 'Меняем':
        b1 = b
        b = a
        a = b1


