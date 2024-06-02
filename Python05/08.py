word = ''
n = 0
cat = -1
number = 1
while word != 'СТОП':
    word = input("Введите текст: ")
    if 'Кот' in word or 'кот' in word:
        n += 1
    if ('Кот' in word or 'кот' in word) and cat == -1:
        cat = number
    number += 1
print(n, cat)