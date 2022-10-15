print("Los números pares e impares")
m7=0
m9=0
for i in range(1000,5001):
    a = i % 7
    b = i % 9
    if a == 0:
        m7 = m7 + 1
    if b == 0:
        m9 = m9 + 1
print(m7)
print(m9)