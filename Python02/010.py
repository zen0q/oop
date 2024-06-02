a = float(input("Введите число 1: "))
b = float(input("Введите число 2: "))
c = str(input("Введите математическую операцию '+,-,*,/': "))
if c != "+" and c != "-" and c != "/" and c != "*":
    print("888888")
elif b == 0 and c == "/":
    print("888888")
elif c == "+":
    print(a + b)
elif c == "-":
    print(a - b)
elif c == "*":
    print(a * b)
elif c == "/":
    print(a / b)
else:
    print("888888")

