coffee = input("How much was your coffee?")
coffee_price = float(coffee)
tax = input("How much was the tax?")
total = coffee_price + tax_price
print(f"Your total is {total}.")

# The answer was incorrect because I did not convert the input values to floats before adding 
# them together. So when I added the two strings together, it concatenated them instead of 
# adding the two values. I fixed the issue by converting the input values to floats
# so that they could be added together correctly.