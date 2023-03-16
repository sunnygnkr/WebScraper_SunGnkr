def validate_Input():
    numRange = range(1, 11)
    inRange = False
    userInput = ''

    # Check whether given input is integer
    while userInput.isdigit() == False or inRange == False:
        userInput = input("Please enter a number between\033[1m 0-10\033[0m: ")
        if not userInput.isdigit():
            print('Sorry , looks like you have entered a\033[1m non-integer\033[0m input')
        # Validate if the number is within an expected range
        if userInput.isdigit():
            if int(userInput) in numRange:
                inRange = True
            else:
                print("Entered input is not within range")

    return int(userInput)


validate_Input()
