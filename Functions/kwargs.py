# Takes multiple arguments in the form of dictionary but not
# exactlty dictionary

def myfunc(**kwargs):
    print(kwargs)
    if 'employment' in kwargs:
    	print('Person is working in {}'.format(kwargs['employment']))
    else:
    	print('No data on persons employment status')

# Also we need to pass the arguments in method argument itself
# since it is not supported in any data structures 

myfunc(name='Sunny',age=29,employment='EY')