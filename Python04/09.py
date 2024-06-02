pir = int(input('Введите высоту пирамиды: '))
for i in range(1, pir + 1, 1):
    print(' ' * (pir - i), '*' * (2 * i - 1))