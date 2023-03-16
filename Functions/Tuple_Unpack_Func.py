def employee_award(empData):

	empName=''
	hoursWorked=0

	for name,time in empData:
		if time>hoursWorked:
			hoursWorked=time
			empName=name
		else:
			pass

	return(empName, hoursWorked)

def emp_Warning(empData):

	empName =''
	minHoursRequired=40

	for name,time in empData:
		if time<minHoursRequired:
			minHoursRequired = time
			empName=name
		else:
			pass

	print(empName+ ' is only working for '+ str(minHoursRequired)+' hours' )

emp_Warning([('Sunny', 30),('Sonam', 50),
 ('Ujwala',55)])

print ("\n")

item = employee_award([('Sunny', 50),('Sonam', 45),
 ('Ujwala',55)])

print(item)