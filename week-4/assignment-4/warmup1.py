#Create a hardcoded list of 8 numbers. Without using any loops, print:
numbers = [10,15,32,49,54,67,76,80]

#The first item
print(f"First: {numbers[0]}")

#The last item (use a negative index)
print(f"Last: {numbers[-1]}")

#A slice containing only the middle four items
print(f"Middle: {numbers[2:6]}")

#The full list in reverse order
print(f"Reversed: {numbers[::-1]}")