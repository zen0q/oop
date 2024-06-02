average = 0
sum = 0
n = int(input('Введите кол-во тестируемых людей: '))
for i in range(n):
    iq = int(input('Введите iq: '))
    sum += iq
    average = sum/(i+1)
    if iq == average:
        print('0')
    elif iq > average:
        print('>')
    else:
        print('<')