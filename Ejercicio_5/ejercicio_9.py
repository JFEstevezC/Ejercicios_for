n=int(input("Escriba la cantidad de números que quiere hallar: "))
s="serie"
for i in range (1,n-1):
	c=i
	i= int((-(-1)** i + 6 * i + 3 ) / 2)
	if c ==  1:
		s = s + " 2, 3, "
	if c == n-1:
		s = s + str(i)
	else :
		s = s + str(i) + ", "
print(s)