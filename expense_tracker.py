# Expense Tracker
# Python project to track daily expenses using JSON file handling

import json

def load_expenses():
    try:
        with open("expenses.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []

def save_expenses(expenses):
    with open("expenses.json", "w") as file:
        json.dump(expenses, file, indent=4)

def add_expense(expenses, item, amount):
    expenses.append({"item": item, "amount": amount})
    save_expenses(expenses)
    print(f"Added expense: {item} - ₹{amount}")

def view_expenses(expenses):
    if not expenses:
        print("No expenses found.")
    else:
        print("\n--- Expense List ---")
        for e in expenses:
            print(f"{e['item']}: ₹{e['amount']}")

def main():
    expenses = load_expenses()
    while True:
        print("\n1. Add Expense\n2. View Expenses\n3. Exit")
        choice = input("Enter your choice: ")
        if choice == "1":
            item = input("Enter expense item: ")
            amount = float(input("Enter amount: "))
            add_expense(expenses, item, amount)
        elif choice == "2":
            view_expenses(expenses)
        elif choice == "3":
            print("Exiting...")
            break
        else:
            print("Invalid choice! Try again.")

if __name__ == "__main__":
    main()
