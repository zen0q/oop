print("Проверка написания логина и резервной почты:")
question1 = "Введите свой корректный логин"
question2 = "Введите свою резервную почту"
print(question1)
answer1 = input()
print(question2)
answer2 = input()
if "@" in answer1 and "@" in answer2:
    print("Некорректный логин")
elif not "@" in answer1 and not "@" in answer2 :
    print("Некорректный адрес")
elif not "@" in answer1 and "@" in answer2:
    print("OK")
elif "@" in answer1 and not "@" in answer2:
    print("Абсолютно неправильно!")