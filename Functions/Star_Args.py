# This helps us take unlimited method arguments
# to take params as tupples

def myfunc(*args):
    print(sum(args)*0.05)

myfunc(50,50,50,50)