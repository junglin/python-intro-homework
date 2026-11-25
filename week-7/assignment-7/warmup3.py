import os

# 1. Print current working directory
print(os.getcwd())

# 2. Check whether expenses.csv exists
if os.path.exists("../data/expenses.csv"):
    print("expenses.csv found.")
else:
    print("expenses.csv not found.")

# 3. Build the file path using os.path.join()
path = os.path.join("..", "data", "expenses.csv")
print(path)
