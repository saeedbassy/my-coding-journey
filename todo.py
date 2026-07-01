choice = "0"
tasks = []
while choice != "3":
    print("1. Add a task")
    print("2. View tasks")
    print("3. Quit")
    choice = input("Choose a number: ")
    if choice == "1":
        user_task = input("Enter a task: ")
        tasks.append(user_task)
    elif choice == "2":
        if len(tasks) == 0:
            print("No tasks yet.")
        else:
            for user_task in tasks:
                    print(user_task)
    elif choice == "3":
        print("Quitting...")
    else:
        print("Invalid choice, please try again.")