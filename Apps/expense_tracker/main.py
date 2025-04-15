import json
import os
import sys

# Defining main functions

def setup_file_paths():
    # folder where the app is
    if getattr(sys, 'frozen', False):
        # Running as a bundled exe
        base_dir = os.path.dirname(sys.executable)
    else:
        # Running as a script
        base_dir = os.path.dirname(os.path.abspath(__file__)) 
        
    data_dir = os.path.join(base_dir, "data") # folder where the data directory is
    file_path = os.path.join(data_dir, "expenses.json")  # folder where 'expenses.json' is
    # create a 'data' directory if there isn't one yet
    os.makedirs(data_dir, exist_ok=True)
    return file_path

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
    if not expenses:
        print("You currently have no expenses in your list.\n")
        
    n = int(input("\nHow many expenses do you want to add?\n"))
    for i in range(n):
        expense_name = input("Enter the expense: ")
        expense_cost = float(input("Enter the cost of the expense: "))
        expenses.append({"Expense": expense_name, "Cost": expense_cost})
    save_expenses(expenses, FILE_PATH)

def rmv_expenses(expenses, FILE_PATH):
    print("Current expense list: \n")
    view_expenses(expenses)
    
    n = int(input("\nHow many expenses do you want to remove?\n"))
    
    for i in range(n):
        try:
            e_id = int(input("Enter the ID number of the expense: "))
            removed = expenses.pop(e_id - 1)
            print(f"Removed: {removed['Expense']} - ${removed['Cost']:.2f}")
        except (ValueError, IndexError):
            print("Invalid ID — skipping.\n")
            
    save_expenses(expenses, FILE_PATH)

        
        
def view_expenses(expenses):
    if not expenses:
        print("Your expense list is EMPTY!\n")
    else:
        total = 0
        print("\n📋 Your Expenses:\n")
        for idx, expense in enumerate(expenses, start=1):
            e_name = expense["Expense"]
            e_cost = expense["Cost"]
            total += e_cost
            print(f"{idx}. {e_name} — ${e_cost:.2f}")
        
        print(f"\n💰 Total spent: ${total:.2f}\n")
    
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
        rmv_expenses(expenses, FILE_PATH)
    elif user_cmd in ["3", "edit"]:
        #edit_expense()
        print("Not Implemented Yet\n")
    elif user_cmd in ["4", "view"]:
        view_expenses(expenses)
        
    else:
        print("Not a supported functionality.\n")
        
   
    
    
    