myFile = open("data.txt")

#Reads the entire file data
data = myFile.read()
print(data+"\n")

# Re-starts the cursor from starting index of the file
myFile.seek(0)

#Reads the entire file in form of list
data2 = myFile.readlines()
print(data2)