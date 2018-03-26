fib = []
n=0
i= int (input ("Enter the number:\n"))
for j in range(2):
	fib.append(1)
for j in range(2, i):
	n = fib[j-1]+fib[j-2]
	fib.append(n)
print (fib)
	