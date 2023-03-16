def isPrime(num):
    if(num<2):
        print(str(num)+' is not a prime')

    for x in range(2,int(num/2)):
        if (num % x)==0:
            print(str(num)+" is not a prime number")
            break
        else:
            print(str(num)+' is a prime')
            break

isPrime(-10)