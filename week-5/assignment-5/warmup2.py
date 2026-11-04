#Use a while loop that repeatedly asks the user to enter a positive integer. 
#If the user enters anything that isn't a positive integer, print a message and ask again. 
#Once valid input is received, print it and stop. 
#The example session below shows the format — your inputs and message wording might differ:
#Enter a positive integer: -3
#That's not a positive integer. Try again.
#Enter a positive integer: hello
#That's not a positive integer. Try again.
#Enter a positive integer: 7
#Got it: 7

while True:
    try:
        user_input = int(input("Enter a positive integer: "))
        if user_input > 0:
            print(f"Got it: {user_input} ")
            break
        else:
            print(f"That's not a positive integer. Try again.")
    except ValueError:
        print("Invalid number, that is not a positive integer. Try again.")
