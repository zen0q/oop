city1 = input("Введите город 1: ")
city2 = input("Введите город 2: ")
if city1 == city2 or city1 == "Тула" and city2 == "Пенза" or city1 == "Пенза" and city2 == "Тула":
    print("Нет")
elif city1 != city2 or city1 == "Тула" and city2 !="Пенза" or city1 =="Пенза" and city2 !="Тула":
    print("Да")
