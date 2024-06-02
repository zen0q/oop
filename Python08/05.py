n = int(input("Введите кол-во строк: "))
collection = []
for i in range(n):
    word = input()
    if word[:3].lower() == "не ":
        word = word[3:]
    collection.append(word)
for collection in collection:
    print(collection)

