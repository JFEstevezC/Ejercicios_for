n = int(input("Digite el número de elementos de la serie: "))
s = "Serie: "
m=2
for i in range(1, n+1):
    if i < n:
        s = s + str (i*m) + ","
        m=m+1
    else:
        s = s + str (i*m)
        m=m+1
print(s)
