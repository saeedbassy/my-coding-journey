contributions = []
choice = "0"

try:
    with open("contributions.txt", "r") as file:
        for contents in file.readlines():
            parts = contents.strip().split("|")
            contributions.append({"date": parts[0], "amount": float(parts[1])})
except:
    pass

while choice != "4":
    print("1. Add a contribution")
    print("2. View contributions")
    print("3. View running total")
    print("4. Quit")
    choice = input("Choose a number: ")
    if choice == "1":
        user_date = input("Enter a date: ")
        user_amount = float(input("Enter an amount: $"))
        new_contribution = {"date": user_date, "amount": user_amount}
        contributions.append(new_contribution)
        with open("contributions.txt", "w") as f:
            for user_contribution in contributions:
                f.write(user_contribution["date"] + "|" + str(user_contribution["amount"]) + "\n")