import string

list1 = [2,5,3,2,3,10,7,4,9]
list2 = [3,6,-5]

def sphereVolume(rad):
    volume=0;

    volume = (4/3)*(3.14)*(rad**3)
    return volume

print(sphereVolume(2))

def inRange(num,hi,low):

    if(num >=low and num <=hi):
        print(str(num)+' is in range')
    else:
        print(str(num) + ' is not in range')

inRange(24, 34, 20)

def checkUpperOrLower(string):
    upperChar=0;
    lowerChar = 0;
    string = string.replace(" ","")
    for char in string:
        if char.isupper():
            upperChar+=1
        else:
            lowerChar+=1

    print('Upper characters: '+ str(upperChar)+' , lower characters: '+ str(lowerChar))

checkUpperOrLower('Sunny Sadu Gaonkar')

def findUnique(listAct):
    set1=set()
    for item in listAct:
        set1.add(item)

    return set1

print(findUnique(list1))

def multiple(listAct):
    mul = 1;

    for item in listAct:
        mul *= item

    return mul

print(multiple(list2))

def pangram(str):
    alphabet = string.ascii_lowercase
    alphaset=set(alphabet)
    set1 = set()

    str = str.replace(" ","").lower()
    for chr in str:
        set1.add(chr)


    if(alphaset==set1):
        print("Given string is a pangram")
    else:
        print("Not a pangram")

pangram("The quick brown fox jumps over the lazy dog")