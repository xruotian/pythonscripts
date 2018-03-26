list = []
for i in range(3):
	value = int (input ("Enter the number:\n"))
	list.append(value)
list.insert(0, 1000)
list.sort()
list.reverse()
print (list)	
