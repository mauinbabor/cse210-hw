import json
from datetime import datetime

# Function to add an expense
def add_expense(expenses, category, amount, date, description):
    expense = {
        "category": category,
        "amount": amount,
        "date": date,
        "description": description
    }
    expenses.append(expense)
    return expenses

# Function to view expenses
def view_expenses(expenses, filter_type=None, filter_value=None):
    if not filter_type:
        return expenses
    if filter_type == "category":
        return [expense for expense in expenses if expense["category"] == filter_value]
    elif filter_type == "date":
        return [expense for expense in expenses if expense["date"] == filter_value]
    return []

# Function to save expenses to a file
def save_expenses(filename, expenses):
    with open(filename, "w") as file:
        json.dump(expenses, file)

# Function to load expenses from a file
def load_expenses(filename):
    try:
        with open(filename, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []

# Function to generate a summary of expenses
def generate_summary(expenses):
    summary = {}
    for expense in expenses:
        category = expense["category"]
        summary[category] = summary.get(category, 0) + expense["amount"]
    total = sum(expense["amount"] for expense in expenses)
    return {"by_category": summary, "total": total}

# Example Test Functions
def test_add_expense():
    expenses = []
    expenses = add_expense(expenses, "Food", 50.0, "2024-12-12", "Groceries")
    assert len(expenses) == 1
    assert expenses[0]["category"] == "Food"
    assert expenses[0]["amount"] == 50.0

def test_generate_summary():
    expenses = [
        {"category": "Food", "amount": 50.0, "date": "2024-12-12", "description": "Groceries"},
        {"category": "Utilities", "amount": 100.0, "date": "2024-12-11", "description": "Electric bill"}
    ]
    summary = generate_summary(expenses)
    assert summary["by_category"]["Food"] == 50.0
    assert summary["by_category"]["Utilities"] == 100.0
    assert summary["total"] == 150.0

if __name__ == "__main__":
    # Example usage
    expenses = []
    expenses = add_expense(expenses, "Food", 50.0, "2024-12-12", "Groceries")
    expenses = add_expense(expenses, "Utilities", 100.0, "2024-12-11", "Electric bill")

    print("All Expenses:", view_expenses(expenses))
    print("Food Expenses:", view_expenses(expenses, "category", "Food"))

    save_expenses("expenses.json", expenses)
    loaded_expenses = load_expenses("expenses.json")
    print("Loaded Expenses:", loaded_expenses)

    summary = generate_summary(expenses)
    print("Expense Summary:", summary)