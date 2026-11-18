#Part 2: Mini-Project — Refactor the Number Cruncher
#Open your mini_project.py from Assignment 5. You're going to refactor it so that each operation 
#lives in its own function.
#Create a new file (don't modify your Week 5 submission). 
#Pull a copy of the numbers list from week-5/data/numbers.py into your new script.
#Define the following functions, each taking numbers (a list) as a parameter:
#find_min(numbers) — returns the minimum value (your loop-based implementation, no min())
#find_max(numbers) — returns the maximum value (your loop-based implementation, no max())
#search(numbers, target) — returns the index of target, or -1 if not found
#bubble_sort(numbers) — returns a new sorted list (do not modify the original)
#show_menu() — prints the menu options and returns the user's choice as a string
#main() — the while loop that calls show_menu() and dispatches to the right function
#Call main() at the bottom of the file.
#Requirements:
#No logic should live outside of a function (except the numbers list definition and the main() call)
#bubble_sort should return a new list, not sort in place
#Your search function should print "Found at index X" or 
#"Not found" from inside main(), not inside search() itself — search just returns the index

numbers = [42, 17, 83, 5, 61, 29, 74, 8, 55, 93, 31, 66, 14, 47, 78, 3, 59, 22, 86, 40]

def find_min(numbers):
    smallest = numbers[0]

    for number in numbers:
        if number < smallest:
            smallest = number
    return smallest

def find_max(numbers):
    biggest = numbers [0]

    for number in numbers:
        if number > biggest:
            biggest = number
    return biggest

def search(numbers, target):
    index = -1

    for i in range(len(numbers)):
        if numbers[i] == target:
            index = i
            break

    return index

def bubble_sort(numbers):
    sorted_numbers = numbers.copy()
    swapped = True
    while swapped:
        swapped = False

        for i in range(len(sorted_numbers)-1):
            if sorted_numbers[i] > sorted_numbers[i+1]:
                sorted_numbers[i], sorted_numbers[i+1] = sorted_numbers[i+1], sorted_numbers[i]
                swapped = True
    return sorted_numbers


def show_menu():
    print("=== Number Cruncher ===")
    print("1. Find minimum")
    print("2. Find maximum")
    print("3. Search for a number")
    print("4. Sort the list")
    print("5. Quit")

    choice = input("Choose an option (1-5): ")
    return choice

def main():
    while True:
        choice = show_menu()
        if choice == "1":
            print(f"Minimum Number: {find_min(numbers)}")
        elif choice == "2":
            print(f"Maximum Number: {find_max(numbers)}")
        elif choice == "3":
            search_num = int(input("Enter a number to search for:"))
            index = search(numbers, search_num)
            if index == -1:
                print("Not found.")
            else:
                print(f"Found at index {index}.")
        elif choice == "4":
            print(f"Sorted Numbers: {bubble_sort(numbers)}.")
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please choose 1-5.")

main()
