duplicates = []


def print_without_duplicates(message):
    if message not in duplicates:
        print(message)
        duplicates.append(message)


def main():
    print_without_duplicates("Привет")
    print_without_duplicates("Не могу до тебя дозвониться")
    print_without_duplicates("Не могу до тебя дозвониться")
    print_without_duplicates("Не могу до тебя дозвониться")
    print_without_duplicates("Когда доедешь до дома")
    print_without_duplicates("Ага, жду")
    print_without_duplicates("Ага, жду")


main()