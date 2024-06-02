M = int(input("Введите кол-во изучающих англ.: "))
N = int(input("Введите кол-во,  изучающих нем.: "))
eng = set()
ger = set()
for i in range(M + N):
    student = input()
    if i < M:
        eng.add(student)
    else:
        ger.add(student)
onelanguage = eng ^ ger
if len(onelanguage):
    print(len(onelanguage))
else:
    print('NO')