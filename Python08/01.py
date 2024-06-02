word = input("Введите слово: ")
minimum = word
maximum = word
while True:
    word = input("Введите слово: ")
    if word == "стоп":
        if len(set(minimum) - set(maximum)) == 0:
            print("ДА")
            break
        else:
            print("НЕТ")
            break

    if len(word) < len(minimum):
         minimum = word
    if len(word) > len(maximum):
         maximum = word





