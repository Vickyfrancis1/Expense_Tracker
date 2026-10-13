import json

def load_expenses():
    try:
        with open("expenses.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []

def save_expenses(expenses):
    with open("expenses.json", "w") as file:
        json.dump(expenses, file)

def add_expense(expenses, description, amount, category):
    expenses.append({
        "description": description.strip().title(),
        "amount": amount,
        "category": category.strip().title()
    })

def category_totals(expenses):
    totals = {}
    for expense in expenses:
        category = expense["category"]
        if category in totals:
            totals[category] = totals[category] + expense["amount"]
        else:
            totals[category] = expense["amount"]
    return totals

expenses = load_expenses()

while True:
    print("\n1. Add expense")
    print("2. Show totals")
    print("3. Show all expenses")
    print("4. Quit")
    choice = input("Choose: ").strip()

    if choice == "1":
        description = input("What did you buy? ")
        while True:
            try:
                amount = float(input("Amount: "))
                break
            except ValueError:
                print("Please type a number.")
        category = input("Category: ")
        add_expense(expenses, description, amount, category)
        save_expenses(expenses)
        print("Added.")
    elif choice == "2":
        if not expenses:
            print("No expenses yet.")
        else:
            totals = category_totals(expenses)
            for category, amount in totals.items():
                print(f"{category}: {amount:,.0f}")
    elif choice == "3":
        if not expenses:
            print("No expenses yet.")
        else:
            for expense in expenses:
                print(f"{expense['description']}: {expense['amount']:,.0f} ({expense['category']})")
    elif choice == "4":
        print("Goodbye!")
        break
    else:
        print("Please choose 1, 2, 3 or 4.")
