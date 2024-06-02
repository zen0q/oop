n = int(input("Введите кол-во строк: "))
cat = False
for i in range(n):
    words = input()
    if 'кот' in words or 'Кот' in words:
        cat = True
    elif "Пёс" in words or "пёс" in words:
        cat = False
if cat:
    print('МЯУ')
else:
    print('НЕТ')