print("Вы проснулись в незнакомом месте. Вы можете пойти вперёд, назад, вправо, влево или остаться на месте")
print("Что же вы выберите?")
choice = input()
if choice == "вперёд":
    print("Вы пришли к деревне")
    print("Что вы хотите сделать дальше? Напасть на неё или попросить помощи у жителей?")
    print("Вам доступны варианты: напасть, попросить помощи")
    choice1 = input()
    if choice1 == "напасть":
        print("Жители оказали вам сопротивление и вы погибли")
    elif choice1 == "попросить помощи":
        print("Жители помогли вам вспомнить где вы живёте и вы смогли добраться до своего дома")
    else:
        print("Ошибка")
elif choice == "назад":
    print("Вы вернулись к себе домой")
elif choice == "вправо":
    print("Вы подошли к большой луже. Вы можете подойти ближе или подумать о своей жизни")
    print("Вам доступны варианты: ближе, подумать")
    choice2 = input()
    if choice2 == "ближе":
        print("Вы поскользнулись и упали лицов в лужу. Вы утонули")
    elif choice2 == "подумать":
        print("Вы вспомнили где ваш дом и вернулись")
    else:
        print("Ошибка")
elif choice == "влево":
    print("Вы подошли к лучшему боксёру деревни. Вы можете вызвать его на бой или убежать")
    print("Вам доступны варианты: бой, убежать")
    choice3 = input()
    if choice3 == "бой":
        print("Вы пропустили удар в голову и вспомнили где живёте. Вы вернулись домой")
    elif choice3 == "убежать":
        print("Вы испугались и мигом вспомнили дорогу домой")
    else:
        print("Ошибка")
elif choice == "остаться на месте":
    print("Вы умерли от старости")
else:
    print("Ошибка")