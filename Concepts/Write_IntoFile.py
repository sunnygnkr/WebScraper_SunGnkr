f = open("myFile.txt","w")

f.writelines(["This data is written\n",
	"Using python code\n"])
# f.close()

with open("myFile.txt",mode='a') as f:
    f.write('New line appended through the code\n')

f.close()

# myFile = open("myFile.txt")
# myFile.seek(0)
# readFile = myFile.read()
# print(readFile)

