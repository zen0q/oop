MES = []


def print_only_new(message):

    if not (message in MES):
        MES.append(message)
        print(message)


def main():
    print_only_new('Шутка номер 15')
    print_only_new('Шутка номер 23')
    print_only_new('Шутка номер 24')
    print_only_new('Шутка номер 24')
    print_only_new('Шутка номер 100')
    print_only_new('Шутка номер 24')
    print_only_new('Шутка номер 99')
    print_only_new('Шутка номер 15')
    print_only_new('Шутка номер 100')


main()
