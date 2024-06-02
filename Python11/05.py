line = input()
list1 = line.split()
print(str('[' + ', '.join('"' + list1[i] + '"' for i in range(len(list1))) + ']'))