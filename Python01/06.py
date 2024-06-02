print("Пожалуйста, отвечайте на вопросы строго да или нет")
question1 = "Вы любите животных?"
question2 = "Вы любите собак?"
print(question1)
answer1 = input()
print(question2)
answer2 = input()
if answer1 == "да" and answer2 == "да":
    print("Вы можете стать дрессировщиком собак")
elif answer1 == "да" and answer2 == "нет":
    print("Вы можете стать дрессировщиклм кошек")
elif answer1 == "нет" and answer2 == "да":
    print("Так собаки тоже животные...")
elif answer1 == "нет" and answer2 == "нет":
    print("Очень жаль, вы нам не подходите")
else:
    print("Отвечайте да или нет")