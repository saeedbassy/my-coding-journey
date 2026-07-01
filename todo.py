tasks = []
choice = "0"

try:
    with open("tasks.txt", "r") as file:
        for contents in file.readlines():
            tasks.append(contents.strip())
except:
    pass

while choice != "3":
    print("1. Add a task")
    print("2. View tasks")
    print("3. Delete a task")
    print("4. Quit")
    choice = input("Choose a number: ")
    if choice == "1":
        user_task = input("Enter a task: ")
        tasks.append(user_task)
        with open("tasks.txt", "w") as f:
            for user_task in tasks:
                f.write(user_task + "\n")
    elif choice == "2":
        if len(tasks) == 0:
            print("No tasks yet.")
        else:
            for index, user_task in enumerate(tasks):
                print(str(index + 1) + ". " + user_task)   
    elif choice == "3":
        for index, user_task in enumerate(tasks):
            print(str(index + 1) + ". " + user_task)
        delete_task = input("Which number do you want to delete? ")
        tasks.pop(int(delete_task) - 1)
        with open("tasks.txt", "w") as f:
            for user_task in tasks:
                f.write(user_task + "\n")
    elif choice == "4":
        print("Quitting...")
        break
    else:
        print("Invalid choice, please try again.")