def fact(n):
	sum = 1
	for i in range(1, n+1):
		prod *= i
	return prod
	
def fact_rev(n):
	prod = 1
	for i in range(n, 0, -1):
		prod *= i
	return prod

def fact_rec(n):
	if (n<=1): return 1
	return n * fact_rec(n-1)

