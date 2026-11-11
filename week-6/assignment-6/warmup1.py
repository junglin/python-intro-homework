# Write a function greet(name, greeting="Hello") that prints a greeting. 
# Call it three different ways:
# With only a name argument
# With both a name and a custom greeting
# With the greeting passed as a keyword argument
# Example output — your name and custom greeting might differ:
#def creates a function, name is a parameter, greeting is another parameter

def greet(name, greeting="Hello, "):
    print(greeting + name + "!")

greet("Jung")
greet("Jung", "Good morning, ")
greet("Jung", greeting="Welcome, ")