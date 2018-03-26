count =0
for i in range(1,5):
	for j in range(1,5):
		for k in range (1,5):
			if (i != j) and (i != k) and (j !=k):
				number = 100*i+10*j+k
				count+=1
				print (number)
print ("The total count of the digitals are:",count)