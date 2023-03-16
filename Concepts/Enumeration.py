# enumerate() is a built-in function 
# which returns a data in tupple form along with the index

myList = [23,54,66,43]

for num in enumerate(myList):
	print(num)

# Above function will print
	# (0, 23)
    # (1, 54)
    # (2, 66)
    # (3, 43)