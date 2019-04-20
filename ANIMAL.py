


def numberchecker():
    # First we prompt the user to enter a number or enter the quit command
    print("Enter Number or enter 'q' to quit:")
    # Next we store our input as a variable called i
    i = input()
    # Then our outer if statement checks if one of 4 quit commands is entered.
    if i == "q" or i == "Q" or i == "Quit" or i == "QUIT" or i == "quit":
        # if the quit command is entered than we print good by and terminate the script by not calling the function again.
        print("Good bye!")
    # We then nest the second if in a try statement just in case the input is not the quit command or convertible into an integer
    else:
        try:
            # We try to convert our input into an integer if this returns a ValueError then we'll jump to the exception
            n = int(i)
            # we check if our input has a remainder of 0 when dividing by 32
            if n % 32 == 0:
                # if that expression is true we print "ANIMAL"
                print("ANIMAL")
                # we then call the function again allowing the user to enter another number without rerunning the script. This is why we included a quit command.
                numberchecker()
            # If the divide by 32 expression is false then we check 16
            elif n % 16 == 0:
                print("ANIM")
                numberchecker()
            # If the divide by 16 expression is false then we check 8
            elif n % 8 == 0:
                print("AN")
                numberchecker()
            # If the divide by 8 expression is false then our number does not meet the requirements.
            else:
                print("Try a diffrent number next time.")
                numberchecker()
        # If our input cannot be converted to int then a ValueError will be returned and will provide an error message.
        except ValueError:
            print("Entry is unacceptable.")
            numberchecker()

#Finally call the function.
numberchecker()