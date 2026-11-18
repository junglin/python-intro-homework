import os
import sys

#1. Use os.path.exists() to verify that ../data/expenses.csv exists before opening it. 
#If it doesn't, print an error message and stop.
if os.path.exists("../data/expenses.csv"):
    print("expenses.csv found.")
else:
    print("expenses.csv not found, there is an error.")
    sys.exit()

#2. Read ../data/expenses.csv into a list of dictionaries using csv.DictReader.
import csv

with open('../data/expenses.csv', 'r') as file:
    reader = csv.DictReader(file)

    my_list = []

    for row in reader:
        my_list.append(row)
        print(f"{row['date']}: {row['category']}, {row['description']}, {row['amount']}")

#3. Convert the amount field to float for each row.
    for row in my_list:
        row['amount'] = float(row['amount'])

#4. Filter the list to only rows where category is "Food".
    food_filter = [row for row in my_list if row['category'] == 'Food']

#5. Calculate the total amount spent on Food.
    total_value = sum(row['amount'] for row in food_filter)
    print(f"Total amount spent on Food: ${total_value:.2f}")

#6. Write a report to food_report.txt with this structure:
from datetime import datetime

with open('food_report.txt', 'w') as file:
    now = datetime.now()

#First line: Food Expense Report — generated [today's date as "Month DD, YYYY"]
    file.write(f'Food Expense Report — generated {now.strftime("%B %d, %Y")}\n')

#One line per food expense: [date]: $[amount]
    for row in food_filter:
        file.write(f'{row['date']}: ${row['amount']:.2f}\n')  

#Last line: Total: $[total to 2 decimal places]
    file.write(f"Total: ${total_value:.2f}\n")   
   

