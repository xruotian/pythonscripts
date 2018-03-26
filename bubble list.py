# bubble list
list = []
temp = 0
len = int (input ("Please enter the no. of the numbers:"))
for i in range (len):
	value = int (input ("Enter the number:\n"))
	list.append(value)

for j in range (len-1):
	for k in range (len-1-j):
		if list[k]>list[k+1]:
			temp = list[k]
			list[k]=list[k+1]
			list[k+1]=temp
print (list)