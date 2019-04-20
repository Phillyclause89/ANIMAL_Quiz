


def numberchecker():
    # First we prompt the user to enter a number or enter the quit command
    print("Enter Number or enter 'q' to quit:")
    # Next we store our input as a variable called i
    i = input()
    # Then our outer if statement checks if one of 4 quit commands is entered.
    if i == "q" or i == "Q" or i == "Quit" or i == "QUIT" or i == "quit":
        # if the quit command is entered than we print good by and terminate the script by not calling the function again.
        print("Good bye!")
    # We then nest the second if stament in a try statement just in case the input is not the quit command or convertible into an integer
    else:
        try:
            # We try to convert our input into an integer
            n = int(i)
            if n % 32 == 0:
                print("ANIMAL")
                numberchecker()
            elif n % 16 == 0:
                print("ANIM")
                numberchecker()
            elif n % 8 == 0:
                print("AN")
                numberchecker()
            else:
                print("Try a diffrent number next time.")
                numberchecker()
        except ValueError:
            print("Entry is unacceptable.")
            numberchecker()


numberchecker()