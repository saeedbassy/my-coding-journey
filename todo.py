tasks = []
choice = "0"

try:
    with open("tasks.txt", "r") as file:
        for contents in file.readlines():
            tasks.append({"text": contents.strip(), "done": False})
except:
    pass

while choice != "6":
    print("1. Add a task")
    print("2. View tasks")
    print("3. Delete a task")
    print("4. Mark task as complete")
    print("5. Edit a task")
    print("6. Quit")
    choice = input("Choose a number: ")
    if choice == "1":
        user_task = input("Enter a task: ")
        new_task = {"text": user_task, "done": False}
        tasks.append(new_task)
        with open("tasks.txt", "w") as f:
            for user_task in tasks:
                f.write(user_task["text"] + "\n")
    elif choice == "2":
        if len(tasks) == 0:
            print("No tasks yet.")
        else:
            for index, user_task in enumerate(tasks):
                if user_task["done"] == True:
                    marker = "X"
                else:
                    marker = " "
                print(str(index + 1) + ". " + "[" + marker + "] " + user_task["text"]) 
    elif choice == "3":
        for index, user_task in enumerate(tasks):
            print(str(index + 1) + ". " + user_task["text"])
        delete_task = input("Which number do you want to delete? ")
        tasks.pop(int(delete_task) - 1)
        with open("tasks.txt", "w") as f:
            for user_task in tasks:
                f.write(user_task["text"] + "\n")
    elif choice == "4":
        for index, user_task in enumerate(tasks):
            print(str(index + 1) + ". " + user_task["text"])
        complete_task = input("Which number do you want to mark complete? ")
        tasks[int(complete_task) - 1]["done"] = True
        with open("tasks.txt", "w") as f:
            for user_task in tasks:
                f.write(user_task["text"] + "\n")
    elif choice == "5":
        for index, user_task in enumerate(tasks):
            print(str(index + 1) + ". " + user_task["text"])
        edit_task = input("Which number do you want to edit? ")
        task_replacement = input("Enter new task: ")
        tasks[int(edit_task) - 1]["text"] = task_replacement
        with open("tasks.txt", "w") as f:
            for user_task in tasks:
                f.write(user_task["text"] + "\n")
    elif choice == "6":
        print("Quitting...")
        break
    else:
        print("Invalid choice, please try again.")