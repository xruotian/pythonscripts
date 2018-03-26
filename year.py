year = int (input ("Enter the year: "))
month = int (input ("Enter the month: "))
day = int (input ("Enter the day: "))

days = [0,31,59,90,120,151,181,212,242,273,303,334]
if 0< month<=12:
	sum = days[month-1]
else:
	print ("data error." )
sum = sum + day

leap = 0
if ((year%4==0) and (year%100!=0)) or (year %400 == 0):
	leap =1

if (leap == 1) and (month >2):
	sum=sum+1

print ("It's the %d day of the year." % sum)
