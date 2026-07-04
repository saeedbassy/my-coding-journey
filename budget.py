expenses = []
choice = "0"

try:
    with open("expenses.txt", "r") as file:
        for contents in file.readlines():
            parts = contents.strip().split("|")
            expenses.append({"amount": float(parts[0]), "category": parts[1]})
except:
    pass

while choice != "6":
    print("1. Add an expense")
    print("2. View expenses")
    print("3. View total spent")
    print("4. View spending by category")
    print("5. Delete an expense")
    print("6. Quit")
    choice = input("Choose a number: ")
    if choice == "1":
        expense_amount = float(input("Enter an expense amount: "))
        expense_category = input("Enter a category: ")
        user_expense = {"amount": expense_amount, "category": expense_category}
        expenses.append(user_expense)
        with open("expenses.txt", "w") as f:
            for user_expense in expenses:
                f.write(str(user_expense["amount"]) + "|" + user_expense["category"] + "\n")
    if choice == "2":
        for index, user_expense in enumerate(expenses, start=1):
            print(str(index) + ". " + "$" + str(user_expense["amount"]) + " " + user_expense["category"])
    if choice == "3":
        total = 0
        for user_expense in expenses:
            total = total + float(user_expense["amount"])
        print("$" + str(total))
    if choice == "4":
        category_totals = {}
        for user_expense in expenses:
            master_category = user_expense["category"]
            category_sum = user_expense["amount"]
            if user_expense["category"] not in category_totals:
                category_totals[master_category] = 0
            category_totals[master_category] = category_totals[master_category] + category_sum
        for master_category in category_totals:
            print("$" + str(category_totals[master_category]) + " " + master_category)
    if choice == "5":
        for index, user_expense in enumerate(expenses, start=1):
            print(str(index) + ". " + "$" + str(user_expense["amount"]) + " " + user_expense["category"])
        delete_expense = input("Enter a nunber to delete: ")
        expenses.pop(int(delete_expense) - 1)
        with open("expenses.txt", "w") as f:
            for user_expense in expenses:
                f.write(str(user_expense["amount"]) + "|" + user_expense["category"] + "\n")