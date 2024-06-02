M = int(input("Введите кол-во изучающих англ.: "))
N = int(input("Введите кол-во,  изучающих нем.: "))
eng = set()
ger = set()
for i in range(M):
    student = input("Ученики изучающие анг.: ")
    eng.add(student)
for i in range(N):
    student = input("Ученики изучающие нем.: ")
    ger.add(student)
onelanguage = eng ^ ger
if len(onelanguage):
    print(len(onelanguage))
else:
    print('NO')