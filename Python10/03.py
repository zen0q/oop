n = int(input("Введите кол-во строк: "))
card = []
for i in range(n):
    words = input("Введите строки для сортировки: ")
    card.append(words)
card.sort()
for _ in range(len(card)):
    print(card[_])