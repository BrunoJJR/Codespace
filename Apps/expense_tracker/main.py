import json
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))  # folder where the app is
DATA_DIR = os.path.join(BASE_DIR, "data") # folder where the data directory is
FILE_PATH = os.path.join(DATA_DIR, "expenses.json") # folder where 'expenses.json' is

os.makedirs(DATA_DIR, exist_ok=True) # create a 'data' directory if there isn't one yet

if os.path.exists(FILE_PATH):
    try:    # try reading as JSON but if decode error start with empty list instead
        with open(FILE_PATH, "r") as file:
            expenses = json.load(file)
    except json.JSONDecodeError:
        expenses = []
else:
    expenses = []

total_cost = 0

for i in range(3):
    expense_name = input("Enter an expense: ")
    expense_cost = float(input("Enter the cost of the expense: "))
    expenses.append({"Expense": expense_name, "Cost": expense_cost})
    total_cost+= expense_cost

for expense in expenses:
    print(f"You have bought {expense['Expense']} for {expense['Cost']}$.")

print(f"\nThat brings us to a grand total of {total_cost}$!")

with open(FILE_PATH, "w") as file:
    json.dump(expenses, file, indent=2)