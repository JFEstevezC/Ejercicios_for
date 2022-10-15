n = int(input("Digite el número de elementos de la serie: "))
s = "Serie: "
m=0
for i in range(1, n+1):
    if i < n:
        s = s + str(i**(i-1)) + "/" + str (i*2 + 1) + ","
    else:
        s = s + str(i**(i-1)) + "/" + str (i*2 + 1)
print(s)