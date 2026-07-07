tasks = []
choice = "0"

try:
    with open("tasks.txt", "r") as file:
        for contents in file.readlines():
            parts = contents.strip().split("|")
            tasks.append({"text": parts[0], "done": parts[1] == "True", "priority": parts[2]})
except:
    pass

while choice != "8":
    print("1. Add a task")
    print("2. View tasks")
    print("3. Delete a task")
    print("4. Mark task as complete")
    print("5. Edit a task")
    print("6. Filter tasks by priority")
    print("7. Search tasks by keyword")
    print("8. Quit")
    choice = input("Choose a number: ")
    if choice == "1":
        user_task = input("Enter a task: ")
        user_priority = input("Enter a priority level (high/medium/low): ")
        new_task = {"text": user_task, "done": False, "priority": user_priority}
        tasks.append(new_task)
        with open("tasks.txt", "w") as f:
            for user_task in tasks:
                f.write(user_task["text"] + "|" + str(user_task["done"]) + "|" + user_task["priority"] + "\n")
    elif choice == "2":
        if len(tasks) == 0:
            print("No tasks yet.")
        else:
            sorted_tasks = sorted(tasks, key=lambda t: t["done"])
            completed_tasks = 0
            for index, user_task in enumerate(sorted_tasks):
                if user_task["done"] == True:
                    marker = "X"
                else:
                    marker = " "
                if user_task["done"] == True:
                    completed_tasks = completed_tasks + 1
                print(f"{index + 1}. [{marker}] {user_task["text"]} ({user_task["priority"]})")
            print(str(completed_tasks) + " of " + str(len(tasks)) + " tasks complete.")
    elif choice == "3":
        for index, user_task in enumerate(tasks):
            print(str(index + 1) + ". " + user_task["text"])
        delete_task = input("Enter a number to delete: ")
        tasks.pop(int(delete_task) - 1)
        with open("tasks.txt", "w") as f:
            for user_task in tasks:
                f.write(user_task["text"] + "|" + str(user_task["done"]) + "|" + user_task["priority"] + "\n")
    elif choice == "4":
        for index, user_task in enumerate(tasks):
            print(str(index + 1) + ". " + user_task["text"])
        complete_task = input("Enter a number to mark complete: ")
        tasks[int(complete_task) - 1]["done"] = True
        with open("tasks.txt", "w") as f:
            for user_task in tasks:
                f.write(user_task["text"] + "|" + str(user_task["done"]) + "|" + user_task["priority"] + "\n")
    elif choice == "5":
        for index, user_task in enumerate(tasks):
            print(str(index + 1) + ". " + user_task["text"])
        edit_task = input("Enter a number to edit: ")
        task_replacement = input("Enter a new task: ")
        tasks[int(edit_task) - 1]["text"] = task_replacement
        with open("tasks.txt", "w") as f:
            for user_task in tasks:
                f.write(user_task["text"] + "|" + str(user_task["done"]) + "|" + user_task["priority"] + "\n")
    elif choice == "6":
        priority_sort = input("Enter a priority level to filter by: ")
        matches = [user_task["text"] for user_task in tasks if user_task["priority"].lower() == priority_sort.lower()]
        print(matches)
    elif choice == "7":
        search_term = input("Enter a keyword to search for: ")
        for user_task in tasks:
            if search_term.lower() in user_task["text"].lower():
                print(user_task["text"])
    elif choice == "8":
        print("Quitting...")
        break
    else:
        print("Invalid choice, please try again.")