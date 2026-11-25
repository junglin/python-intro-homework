#Ask the user for two numbers. Compute the result of dividing the first by the second. 
#Use try/except ZeroDivisionError to catch division by zero and print a friendly message 
#instead of crashing. The example sessions below show the format for two different inputs 
#— your numbers and message wording might differ:

try:
    number_one = int(input("Enter the numerator:"))
    number_two = int(input("Enter the denominator:"))
    answer = number_one / number_two
    print(f"{number_one} ÷ {number_two} = {answer:.1f}")

except ZeroDivisionError:
    print(f"Can't divide by zero — please try a non-zero denominator.")