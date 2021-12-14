from math import factorial as fact

def nCr(n,r):
	return fact(n) // (fact(r) * fact(n-r))

def PascelTriangle(n):
	for row in range(0, n) :
		for col in range(0, row + 1):
		    print(nCr(row,col), end= "  ")
		print()

n = int(input("Enter line number: "))
PascelTriangle(n)
print("Pascel Triangle with combination")
