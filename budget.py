expenses = []
choice = "0"
valid_categories = ("food", "gas", "entertainment", "bills", "other")

try:
    with open("expenses.txt", "r") as file:
        for contents in file.readlines():
            parts = contents.strip().split("|")
            expenses.append({"amount": float(parts[0]), "category": parts[1]})
except:
    pass

while choice != "8":
    print("1. Add an expense")
    print("2. View expenses")
    print("3. View total spent")
    print("4. View spending by category")
    print("5. Delete an expense")
    print("6. Edit an expense")
    print("7. Search expenses by category")
    print("8. Quit")
    choice = input("Choose a number: ")
    if choice == "1":
        expense_amount = float(input("Enter an expense amount: $"))
        if expense_amount > 0:
            expense_category = input("Enter a category (food/gas/entertainment/bills/other): ")
            if expense_category.lower() in valid_categories:
                user_expense = {"amount": expense_amount, "category": expense_category}
                expenses.append(user_expense)
                with open("expenses.txt", "w") as f:
                    for user_expense in expenses:
                        f.write(str(user_expense["amount"]) + "|" + user_expense["category"] + "\n")
            else:
                print("Invalid category!")
        else:
            print("Invalid expense amount!")
    elif choice == "2":
        for index, user_expense in enumerate(expenses):
            print(f"{index + 1}. ${user_expense["amount"]:.2f} {user_expense["category"]}")
    elif choice == "3":
        total = 0
        for user_expense in expenses:
            total = total + float(user_expense["amount"])
        print(f"${total:.2f}")
    elif choice == "4":
        category_totals = {}
        for user_expense in expenses:
            master_category = user_expense["category"]
            category_sum = user_expense["amount"]
            if user_expense["category"] not in category_totals:
                category_totals[master_category] = 0
            category_totals[master_category] = category_totals[master_category] + category_sum
        for master_category in category_totals:
            print("$" + str(category_totals[master_category]) + " " + master_category)
    elif choice == "5":
        for index, user_expense in enumerate(expenses):
            print(f"{index + 1}. ${user_expense["amount"]:.2f} {user_expense["category"]}")
        delete_expense = input("Enter a nunber to delete: ")
        expenses.pop(int(delete_expense) - 1)
        with open("expenses.txt", "w") as f:
            for user_expense in expenses:
                f.write(str(user_expense["amount"]) + "|" + user_expense["category"] + "\n")
    elif choice == "6":
        for index, user_expense in enumerate(expenses):
            print(f"{index + 1}. ${user_expense["amount"]:.2f} {user_expense["category"]}")
        edit_expense = input("Enter a number to edit: ")
        expense_amount_replacement = input("Enter a new amount: $")
        expense_replacement = input("Enter a new expense category: ")
        if expense_replacement.lower() in valid_categories:
            expenses[int(edit_expense) - 1]["amount"] = float(expense_amount_replacement)
            expenses[int(edit_expense) - 1]["category"] = expense_replacement
            with open("expenses.txt", "w") as f:
                for user_expense in expenses:
                    f.write(str(user_expense["amount"]) + "|" + user_expense["category"] + "\n")
        else:
            print("Invalid category!")
    elif choice == "7":
        search_category = input("Enter a category to search: ")
        matches = [f"{index + 1}. ${user_expense['amount']:.2f} {user_expense['category']}" for user_expense in expenses if search_category.lower() == user_expense["category"].lower()]
        print(matches)