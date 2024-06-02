words = ""
count = 0
a = 0
while words != "стоп":
    count += 1
    words = input("Введите предложения: ")
    if "Кот" in words or "кот" in words:
        a = a + count
        break
if a == 0:
    print("-1")
else:
    print(a)