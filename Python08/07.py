n = int(input("Введите кол-во строк: "))
collection = []
for i in range(n):
    word = input()
    if "кот" in word:
        index = word.index("кот") + 1
        collection.append((i + 1, index))
for words in collection:
    print(words[0], words[1])