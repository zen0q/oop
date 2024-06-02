M = int(input("Книг в дом.библиотеке: "))
N = int(input("Книг в списке на лето: "))
library = set()
listbook = set()
for i in range(M):
    book = input("Название книги в дом.библиотеке: ")
    library.add(book)
for i in range(N):
    book = input("Название книги в списке на лето: ")
    listbook.add(book)
    if book in library:
        print('YES')
    else:
        print('NO')