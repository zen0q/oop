n = int(input('Введите количество натуральных чисел: '))
if n <= 0:
    print('Введите число, где (n > 0): ')
else:
    sum = 0
    for i in range(n):
        num = int(input("Введите число: "))
        if i % 2 == 0:
            sum += num
        else:
            sum -= num
    print('Сумма знакочередующаяся ряда: ', sum)