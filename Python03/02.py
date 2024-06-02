password1 = input("Enter your password: ")
password2 = input("Enter one more: ")
while password1 == password2 and len(password1) < 8:
    print("Короткий")
    password1 = input("Enter your password: ")
    password2 = input("Enter one more: ")
    while password1 != password2 and len(password1):
        print('vary')
        password1 = input("Enter your password: ")
        password2 = input("Enter one more: ")
while password1 != password2 and len(password1):
    print('vary')
    password1 = input("Enter your password: ")
    password2 = input("Enter one more: ")
    while password1 == password2 and len(password1) < 8:
        print("Короткий")
        password1 = input("Enter your password: ")
        password2 = input("Enter one more: ")
if password1 == password2 and len(password1) >= 8:
    print('Ok')


