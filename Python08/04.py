n = int(input("Введите размер доски: "))
a = []
b = "ABCDEFGHI"

if n < 9:
    a = [[c + 1 for c in range(9)] for i in range(9)]

for i in range(n)[::-1]:
    for c in range(n):
        print(b[c] + str(a[c][i]), end=' ')
    print()





