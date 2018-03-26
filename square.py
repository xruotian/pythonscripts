import math
for i in range (10000000000):
	x = int (math.sqrt(i+1000))
	y = int (math.sqrt(i+2680))
	if (x*x ==i+1000) and (y*y == i +2680):
		print (i)