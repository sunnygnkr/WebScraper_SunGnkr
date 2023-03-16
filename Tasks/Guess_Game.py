from random import shuffle

list = ['','O','']

def shuffle_ball():
	shuffle(list)
	return list

def userInput():
	userInput = ''

	while userInput not in ['0','1','2']:
		userInput = input("Please guess the index "+ 
			"between 0 or 1 or 2\n")

	return int(userInput)

def checkResult(game, usrInp):

	if game[usrInp]!='O':
		print("Your guess is wrong")
		return False
	else:
		print("You guessed the right answer")
		return True

guess = userInput()
list = shuffle_ball()
print("After shuffling: "+ str(list))
checkResult(list, guess)