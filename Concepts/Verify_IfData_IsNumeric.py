# We use isDigit() functionn here

def validateData():
    choice=''

    while choice.isdigit()==False:
        choice = input("Please enter a digit: ")

    return choice

print(validateData())