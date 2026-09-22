name=input("ФИО: ")
print(f"ФИО: {name}")
words=name.split()
inic=words[0][0]+words[1][0]+words[2][0]
le=len(words[0])+len(words[1])+len(words[2])
print(f"Инициалы: {inic}.")
print(f"Длина (символов): {le+2}")