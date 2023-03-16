
def combo(*args, **kwargs):

	first_val = list(kwargs.values())[1]

	if(args[0]==1):
		print('Args is higher priority')
	elif(first_val ==29):
		print('kwargs is leading')
	else:    
	    print("Both are not into consideration")
	

combo(0,1,name='Funny',age=29)