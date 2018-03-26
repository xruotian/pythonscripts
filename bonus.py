salary = int (input ("please enter the totoal number: "))
print ("the salary you entered is:", salary)
if salary > 1000000:
	bonus = (salary - 1000000)*0.01 +400000*0.015+ +200000*0.03+200000* 0.05+ 100000*0.075+100000*0.1
	print ("The bounus you will get is: ", bonus)

if 1000000> salary > 600000:
	bonus = (salary - 600000)*0.015 +200000*0.03 +200000* 0.05+ 100000*0.075+100000*0.1
	print ("The bounus you will get is: ", bonus)	
	
if 600000 > salary > 400000:
	bonus = (salary - 400000)*0.03 + 200000* 0.05+ 100000*0.075+100000*0.1
	print ("The bounus you will get is: ", bonus)	

if 400000> salary > 200000:
	bonus = (salary - 200000)*0.05 + 100000*0.075+100000*0.1
	print ("The bounus you will get is: ", bonus)	
	
if 200000 >salary > 100000:
	bonus = (salary - 100000)*0.075+100000*0.1
	print ("The bounus you will get is: ", bonus)


