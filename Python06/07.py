M = int(input("Введите кол-во листков: "))
N = int(input("Введите кол-во блоков: "))
every = set(input() for i in range(N))
for i in range(1, M):
    list = set(input() for i in range(N))
    every = every & list
for names in every:
    print(names)