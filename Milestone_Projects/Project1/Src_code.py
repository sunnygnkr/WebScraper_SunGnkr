# global numRange
numRange = [0, 1, 2]

def display_gameList(range_num):
    print(range_num)

# Function1
def user_Choice():
    userInput = ''
    while userInput not in ['0', '1', '2']:
        userInput = input('Please enter integers in range of 0-2: ')
        if not userInput.isdigit():
            print('Invalid choice! Please enter input in integer format')
    return int(userInput)

# Function2 dependant on Function1
def replace_Userchoice(num_Range,userChoice):
    newInput = input("Please enter the new string to replace the existing one: ")

    num_Range[userChoice] = newInput

    return num_Range

# Function3
def gameon_choice():
    choice = 'wrong'

    while choice not in ['Y','N']:
        choice=input('Keep playing? (Y or N) ')

        if choice not in ['Y','N']:
            print('Either select Y to continue playing or N to quit the game')

    if choice == 'Y':
        return True
    else:
        return False

# Final game source-code

game_on = True
while game_on :
    display_gameList(numRange)
    userChoice = user_Choice()
    numRange = replace_Userchoice(numRange,userChoice)
    display_gameList(numRange)
    game_on = gameon_choice()