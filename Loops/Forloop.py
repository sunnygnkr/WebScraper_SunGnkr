count =0;

for x in range(10):
	count+=1

print(count)

# Printing elements in the same line
itr  = [1,2,3]

for items in itr:
	print(items, end =" ")

print("\n")

# Using for loops to iterate thorugh a dictionary
myPair ={'name':"Sunny", 'age':29, 'sex': 'M'}

for key,val in myPair.items():
    print(val) 
