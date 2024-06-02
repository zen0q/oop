def triangle(a, b, c):
    if a + b <= c or a + c <= b or b + c <= a:
        print("Это не треугольник")
    else:
        print("Это треугольник")


triangle(7, 6, 10)