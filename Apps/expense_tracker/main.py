import json
import os

# Defining main functions

def setup_file_paths():
    BASE_DIR = os.path.dirname(os.path.abspath(
    __file__))  # folder where the app is
    DATA_DIR = os.path.join(BASE_DIR, "data")  # folder where the data directory is
    # folder where 'expenses.json' is
    FILE_PATH = os.path.join(DATA_DIR, "expenses.json")
    # create a 'data' directory if there isn't one yet
    os.makedirs(DATA_DIR, exist_ok=True)
    return FILE_PATH

def load_expenses(FILE_PATH):
    if os.path.exists(FILE_PATH):
        try:    # try reading as JSON but if decode error start with empty list instead
            with open(FILE_PATH, "r") as file:
                return json.load(file)
        except json.JSONDecodeError:
            return []
    else:
        return []

def save_expenses(expenses, FILE_PATH):
    with open(FILE_PATH, "w") as file:
        json.dump(expenses, file, indent=2)
        
def add_expenses(expenses, FILE_PATH):
    n = int(input("How many expenses do you want to add?\n"))
    for i in range(n):
        expense_name = input("Enter the expense: ")
        expense_cost = float(input("Enter the cost of the expense: "))
        expenses.append({"Expense": expense_name, "Cost": expense_cost})
    save_expenses(expenses, FILE_PATH)
        
# main variables
FILE_PATH = setup_file_paths()  
expenses = load_expenses(FILE_PATH)

# Main CLI Menu
while True:
    print("Options: 1 - Add Expense; 2 - Remove Expense; 3 - Edit Expense; 4 - View Expenses; 5 - Quit")
    user_cmd = input()
    
    if user_cmd in ["5", "quit"]:
        break
    
    elif user_cmd in ["1", "add"]:
        add_expenses(expenses, FILE_PATH)
        
    elif user_cmd in ["2", "rmv"]:
        #rmv_expense()
        print("Not Implemented Yet")
    elif user_cmd in ["3", "edit"]:
        #edit_expense()
        print("Not Implemented Yet")
    elif user_cmd in ["4", "view"]:
        #view_expense()
        print("Not Implemented Yet")
        
    else:
        print("Not a supported functionality.\n")
        
   
    
    
    