#Write a script that attempts to open ../data/missing.txt (this file does not exist). 
#Use try/except FileNotFoundError to catch the error and print a helpful message rather than a traceback.
#The example below shows the format — your message wording might differ:
#Error: "missing.txt" was not found. Please check the file path and try again.

try:
    with open("../data/missing.txt", "r") as f:
        content = f.read()
        print(content)

except FileNotFoundError:
    print("Error: '../data/missing.txt' was not found. Please check the file path and try again.")
