n = int(input("Digite el número de elementos de la serie: "))
s = "Serie: "
for i in range(1, n+1):
    if i < n:
        s = s + "1/" + str (i) + ","
    else:
        s = s + "1/" + str (i)
print(s)