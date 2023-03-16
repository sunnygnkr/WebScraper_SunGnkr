string = "Sunny is a smart guy"
list1 = string.split()

# Normal for_loop
for char in list1:
	if(char[0].lower()=='s'):
		print(char)
    
print("\n")

# Now using the list_comprehension

char = [x for x in list1 if x[0].lower()=='s']
print(char)

# help()