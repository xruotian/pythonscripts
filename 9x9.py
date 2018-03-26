# print 9*9
for i in range(10):
	for j in range(1,i+1):
		print("%dx%d=%2d" %(i,j,i*j),end=" ")
	print ("")