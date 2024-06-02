check = 0
while check == 0:
    password1 = input("Enter your password: ")
    password2 = input("Enter one more: ")
    if len(password1) < 8:
        print('short')
    elif "123" in password1:
        print('simple')
    elif password1 != password2:
        print('vary')
    else:
        print('OK')