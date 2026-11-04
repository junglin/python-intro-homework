#Start with a hardcoded list of names. 
#Ask the user to enter a name. 
#Loop through the list and print whether the name was found and at what index 
#— or a not-found message if it isn't in the list. 
#The examples below show the format for two different searches 
#— your names, index, and message wording might differ:

names = ["Wendy", "Ronald", "Cane", "Jack", "Kernel"]
name_input = input("Enter a name to search for: ")
target = name_input
index = -1
found = False

for i in range(len(names)):
    if names[i] == target:
        found = True
        index = i
        break
if found:
    print(f"Name to search for: {name_input}")
    print(f"Found {name_input} at index {i}")
else:
    print(f"{name_input} not in the list.")



