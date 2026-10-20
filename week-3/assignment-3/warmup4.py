number = int(input("Enter a number:"))

#Block 1: Sign
if number > 0:
    print(f"{number} is positive.")
elif number < 0:
    print(f"{number} is negative.")
else:
    print(f"{number} is neither positive or negative.")

#Block 2: Parity
if number % 2 == 0:
    print(f"{number} is even.")
else:
    print(f"{number} is odd.")