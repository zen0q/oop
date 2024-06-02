M = int(input())
menu = set()
cook = set()
for i in range(M):
    name = input()
    menu.add(name)
N = int(input())
for i in range(N):
    num = int(input())
    for i in range(num):
        name = input()
        if name not in cook:
            cook.add(name)
difference = menu - cook
for i in difference:
    print(i)