max_len = int(input("Введите максимальную длину: "))
n = int(input("Кол-во заголовков: "))
for i in range(n):
    title = input()
    if len(title) <= max_len:
        print(title)
    else:
        new_title = title[: max_len - 3] + "..."
        print(new_title)