n = int(input("Введите кол-во строк: "))
count = 0
for i in range(n):
    word = input("Введите строки: ")
    count += 1
    if "кот" in word:
        print(count, word.find("кот") + 1)