#Use a for loop with range() to calculate the 
#sum of all integers from 1 to 100. Print the result.
#Example output — your message wording might differ:
#The sum of 1 to 100 is 5050.

#start by setting the variable and holds the running sum of everything added so far
total = 0
# i holds the current number
for i in range(1,101):
    total += i   #same thing as total = total + i
print(f"The sum of 1 to 100 is {total}!")