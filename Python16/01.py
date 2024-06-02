PI = 3.14159


def circle_length(radius: int):
    return 2 * PI * radius


def circle_area(radius: int):
    return PI * radius ** 2


def main():

    print(circle_length(5))
    print(circle_area(10))


main()


