a = int(input("Введите число a, где a < b: "))
b = int(input("Введите число b, где b > a: "))
if a > b:
    print("a должно быть меньше b!")
for i in range(a, b + 1):
    if i % 3 == 0 and i % 5 == 0 :
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)