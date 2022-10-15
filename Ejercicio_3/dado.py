import random
print("Dados")
n1 = ""
n2 = ""
n3 = ""
n4 = ""
n5 = ""
n6 = ""

n=int(input("Esciba las veces que desee que lance el dado: "))
for i in range(n):
    ale=random.randint(1,6)
    if ale == 1:
        n1 = n1 + "*"
    elif ale == 2:
        n2 = n2 + "*"
    elif ale == 3:
        n3 = n3 + "*"
    elif ale == 4:
        n4 = n4 + "*"
    elif ale == 5:
        n5 = n5 + "*"
    elif ale == 6:
        n6 = n6 + "*"
print("El número 1 salió",n1,"veces")
print("El número 2 salió",n2,"veces")
print("El número 3 salió",n3,"veces")
print("El número 4 salió",n4,"veces")
print("El número 5 salió",n5,"veces")
print("El número 6 salió",n6,"veces")