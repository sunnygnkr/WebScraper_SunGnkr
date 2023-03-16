import os

# Get the current working directory
cwd = os.getcwd()
print(cwd)

'''
def myfunc(string):
    
    newString=''
 
# Finding index of each character in String   

    for index,char in enumerate(string):
        print (index)
        if ((index+1) %2 == 0):
            newString=newString+char.upper()
        elif((index+1) %2 != 0):
            newString=newString+char.lower()
        else:
        	pass
            
    return newString
   
'''

'''
def myfunc1(num):
    val = abs(100-num) //Returns the absolute(positive) value
    print(val)
'''

'''
def myfunc2(a, b, c):
    if (a + b + c <= 21):
        return a + b + c
    elif (a + b + c >= 21 and (a == 11 or b == 11 or c == 11)):
        return (a + b + c) - 10
    else:
        return 'BUST'
'''

'''
listData = [2,2,5,6,7,9,-2,4]

def myFunc3(list):
    sum=0
    temp=True

    for item in list:

        while temp:  #temp==true
            if(item!=6):
                sum += item
                break      #Comes out of while loop
            else:
                temp=False

        while not temp:
            if (item!=9):
                break     #Comes out of while loop
            else:
                temp=True
                break     #Comes out of while loop
    return sum
    
print(myFunc3(listData))
'''



