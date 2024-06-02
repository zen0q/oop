word1 = input("Введите слово 1: ")
word2 = input("Введите слово 2: ")
bull = 0
cow = 0
for i in set(word1) & set(word2):
    if word1.index(i) == word2.index(i):
        bull += 1
    else:
        cow += 1
print(bull, cow)