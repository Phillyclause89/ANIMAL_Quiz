


def numberchecker():
    print("Enter Number or Press q to quit:")
    i = input()
    if i == "q":
        print("Good bye!")
    else:
        try:
            n = int(i)
            if i == "q":
                print("Good bye!")
            elif n % 32 == 0:
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