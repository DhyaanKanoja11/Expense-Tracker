# Expense Tracker (Beginner Level) with Improved Variable Names

# Initialize variables
total_income = 0
expense_records = []

while True:
    print("\nExpense Tracker Menu:")
    print("1. Add Income")
    print("2. Add Expense")
    print("3. View Expenses")
    print("4. View Categories")
    print("5. View Monthly Report")
    print("6. Quit")

    choice = input("Enter your choice (1/2/3/4/5/6): ")

    if choice == "1":
        income_amount = float(input("Enter income amount: $"))
        total_income += income_amount
        print(f"Income of ${income_amount} added.")
    elif choice == "2":
        expense_category = input("Enter expense category: ")
        expense_description = input("Enter expense description: ")
        expense_amount = float(input("Enter expense amount: $"))
        expense_records.append({"category": expense_category, "description": expense_description, "amount": expense_amount})
        print(f"Expense of ${expense_amount} added.")
    elif choice == "3":
        total_expenses = sum(expense["amount"] for expense in expense_records)
        print("\nExpense Tracker")
        print(f"Income: ${total_income}")
        print("Expenses:")
        for expense in expense_records:
            print(f"Category: {expense['category']}, Description: {expense['description']}, Amount: ${expense['amount']}")
        print(f"Total Expenses: ${total_expenses}")
    elif choice == "4":
        expense_categories = set(expense["category"] for expense in expense_records)
        print("\nExpense Categories:")
        for category in expense_categories:
            print(category)
    elif choice == "5":
        total_expenses = sum(expense["amount"] for expense in expense_records)
        print("\nMonthly Report")
        print(f"Income: ${total_income}")
        print(f"Total Expenses: ${total_expenses}")
        if total_expenses > 0:
            print(f"Savings: ${total_income - total_expenses}")
    elif choice == "6":
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")
