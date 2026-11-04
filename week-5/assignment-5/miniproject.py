#Requirements for each option:
#Find minimum — loop through the list and track the smallest value. Do not use Python's built-in min().
#Find maximum — same approach, tracking the largest value. Do not use max().
#Search — ask the user for a number, then implement a linear search loop. Print the index if found, or a "not found" message.
#Sort — implement bubble sort: repeatedly loop through adjacent pairs, swap if out of order, and repeat until no swaps occur. Print the sorted list. Do not use sorted() or .sort().
#Quit — print a goodbye message and exit the loop.
#The menu should redisplay after each operation until the user chooses Quit.

numbers = [42, 17, 83, 5, 61, 29, 74, 8, 55, 93, 31, 66, 14, 47, 78, 3, 59, 22, 86, 40]

while True:

    print("=== Number Cruncher ===")
    print("1. Find minimum")
    print("2. Find maximum")
    print("3. Search for a number")
    print("4. Sort the list")
    print("5. Quit")

    user_input = int(input("Choose an option (1-5):"))

    #if the user decides on option 1
    if user_input == 1:
        #the smallest number is the first number of the list.
        smallest = numbers[0]
        #defining the variable number in the list of numbers
        for number in numbers:
            #if the number is smaller than the first number in the index then the number is now the smallest
            if number < smallest:
                #reassigning the number to the smallest
                smallest = number
        #printing outside of the if loop
        print(f"Minimum number: {smallest}")
    
    elif user_input == 2:
        biggest = numbers[0]
        for number in numbers:
            if number > biggest:
                biggest = number
        print(f"Maximum number: {biggest}")
    
    elif user_input == 3:
        search_num = int(input("Enter a number to search for:"))
        target = search_num
        index = -1
        found = False
        
        #loop through every index (position) in the list
        for i in range(len(numbers)):
            if numbers[i] == target:
                found = True
                index = i
                break
        
        if found:
            print(f"The number to search for: {search_num}")
            print(f"Found {search_num} at index {index}")
        else:
            print(f"{search_num} is not in the list.") 
    
    elif user_input == 4:
        def bubble_sort(data):
            swapped = True
            while swapped:
                swapped = False
                for i in range(len(data)-1):
                    if data[i] > data[i+1]:
                        data[i], data[i+1] = data[i+1], data[i]
                        swapped = True
            return data
        print(bubble_sort(numbers))

    elif user_input ==5: 
        print("Goodbye!")
        break
 
 