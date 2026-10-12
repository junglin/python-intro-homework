coffee = input("How much was your coffee?")
coffee_price = float(coffee)
tax = input("How much was the tax?")
tax_price = float(tax)
total = coffee_price + tax_price
print(f"Your total is {total}.")

# 1. Error Message pasted below:
# Traceback (most recent call last):
# File "/Users/jung.lin@kippking.org/new_rep/python-intro-homework/week-2/assignment-2/warmup4.py", line 4,in <module>
# total = coffee_price + tax_price
#                           ^^^^^^^^^
# NameError: name 'tax_price' is not defined
# 2. The issue was I did not define the tax_price variable.
# I also didn't convert the input values to floats before adding the coffee_price and tax_price together.
# 3. I fixed the issue by converting the input values to floats
# so that they could be added together correctly instead of being concatenated as strings.