print("Ejercicio 1")
for i in [1,2,3,4,5]:
    print(1)
print("Ejercicio 2")
for i in (1,2,3,4,5):
    print(i)
print("Ejercicio 3")
lista=[1,2,3,4,5]
for i in lista:
    print (i)
print("Ejercicio 4")

for i in range(1,6):
    print(i)

print("Ejercicio 5")
texto = "UIS no es uno, somos todos"
for i in texto:
    print(i)

print("Ejercicio 6")
suma = 0
for i in range(10):
    suma = suma + i
print(suma)
print("Ejercicio 7")
N = int(input("Escriba los N número que quiere sumar"))
suma = 0
for i in range(1,N+1):
    suma = suma + i
print(suma)
print("Ejercicio 8: Contar vocales en una frase")
frase=input("Digite una frase ")
base = "aeiouAEIOU"
num_vocales = 0
for i in frase:
    if i in base:
        num_vocales = num_vocales + 1

print("El número de vocales es " + str(num_vocales))