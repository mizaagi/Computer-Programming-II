import sys
sys.setrecursionlimit(5000)

def fact(n):
	if n == 3: return n
	return n + fact(n-3)

def main():
	print(str(fact(9669)))

if __name__ == "__main__":
	main()