left = 0
right = 1001
current = (left + right) // 2
answer = None

while answer != '=':
    print(current, '?')
    answer = input()

    if answer == '=':
        print('Я угадал!')
        break
    elif answer == '>':
        left = current
    elif answer == '<':
        right = current
    else:
      print('Повторите ввод (>, <, =)!')
      continue

    current = int((left + right) // 2)
