x = int (input ("Enter the first number: "))
y = int (input ("Enter the second number: "))
z = int (input ("Enter the third number: "))
va1 = va2 =va3=va4=va5=va6= 0
if x<y: 
	va1 = y
	va2 = x
else:
	va1 = x
	va2 = y
if va1<z:
	va3 = z
	va4=va1
else:
	va3=va1
	va4= z
	
if va2<va4:
	va5 = va4
	va6 = va2
else:
	va5 = va2
	va6 = va4

print ("The sequences from biggest to smallest are:", va3,va5,va6)
		
