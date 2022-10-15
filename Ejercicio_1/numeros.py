print("Los números pares e impares")
pares=0
impares=0
for i in range(100):
    n = int(input("Ingrese un número: "))
    m = n % 2
    if m == 0:
        pares = pares + 1
    else:
        impares = impares + 1 
print ("La cantidad de números pares es: ",pares)
print ("La cantidad de números impares es: ",impares)