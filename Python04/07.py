count = 0
a = int(input())
for i in range(1, a + 1):
    if a % i == 0:
        if i != a:
            print(str(i), end=" ")
        if i == a:
            print(str(i))
        count += 1
if a == 1:
    print("НЕТ")
elif count == 2:
    print("ПРОСТОЕ")
else:
    print("НЕТ")