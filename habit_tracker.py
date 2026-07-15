habits = []
choice = "0"
invalid_habit = ""

try:
    with open("habits.txt", "r") as file:
        for contents in file.readlines():
            parts = contents.strip().split("|")
            habits.append({"text": parts[0], "status": {"completion": parts[1] == "True", "streak_count": int(parts[2])}})
except:
    pass

while choice != "6":
    print("1. Add a habit")
    print("2. View habits")
    print("3. Mark a habit as done today")
    print("4. Reset a habit's completion")
    print("5. Delete a habit")
    print("6. Quit")
    choice = input("Choose a number: ")
    if choice == "1":
        user_habit = input("Enter a habit: ")
        if user_habit != invalid_habit:
            new_habit = {"text": user_habit, "status": {"completion": False, "streak_count": 0}}
            habits.append(new_habit)
            with open("habits.txt", "w") as f:
                for user_habit in habits:
                    f.write(user_habit["text"] + "|" + str(user_habit["status"]["completion"]) + "|" + str(user_habit["status"]["streak_count"]) + "\n")
        else:
            print("Invalid habit!")
    elif choice == "2":
        if len(habits) == 0:
            print("No habits yet.")
        else:
            for index, user_habit in enumerate(habits):
                if user_habit["status"]["completion"] == True:
                    marker = "X"
                    print(f"{index + 1}. [{marker}] {user_habit["text"]} 🔥 {user_habit["status"]["streak_count"]}")
                else:
                    marker = " "
                    print(f"{index + 1}. [{marker}] {user_habit["text"]} 🔥 {user_habit["status"]["streak_count"]}")
    elif choice == "3":
        for index, user_habit in enumerate(habits):
            if user_habit["status"]["completion"] == True:
                marker = "X"
                print(f"{index + 1}. [{marker}] {user_habit["text"]} 🔥 {user_habit["status"]["streak_count"]}")
            else:
                marker = " "
                print(f"{index + 1}. [{marker}] {user_habit["text"]} 🔥 {user_habit["status"]["streak_count"]}")
        mark_done = input("Enter a number to mark as done today: ")
        habits[int(mark_done) - 1]["status"]["completion"] = True
        habits[int(mark_done) - 1]["status"]["streak_count"] = habits[int(mark_done) - 1]["status"]["streak_count"] + 1
        with open("habits.txt", "w") as f:
            for user_habit in habits:
                f.write(user_habit["text"] + "|" + str(user_habit["status"]["completion"]) + "|" + str(user_habit["status"]["streak_count"]) + "\n")
    elif choice == "4":
        for index, user_habit in enumerate(habits):
            if user_habit["status"]["completion"] == True:
                marker = "X"
                print(f"{index + 1}. [{marker}] {user_habit["text"]} 🔥 {user_habit["status"]["streak_count"]}")
            else:
                marker = " "
                print(f"{index + 1}. [{marker}] {user_habit["text"]} 🔥 {user_habit["status"]["streak_count"]}")
        reset_habit = input("Enter a number to reset its completion: ")
        habits[int(reset_habit) - 1]["status"]["completion"] = False
        with open("habits.txt", "w") as f:
            for user_habit in habits:
                f.write(user_habit["text"] + "|" + str(user_habit["status"]["completion"]) + "|" + str(user_habit["status"]["streak_count"]) + "\n")
    elif choice == "5":
        for index, user_habit in enumerate(habits):
            if user_habit["status"]["completion"] == True:
                marker = "X"
                print(f"{index + 1}. [{marker}] {user_habit["text"]} 🔥 {user_habit["status"]["streak_count"]}")
            else:
                marker = " "
                print(f"{index + 1}. [{marker}] {user_habit["text"]} 🔥 {user_habit["status"]["streak_count"]}")
        delete_habit = input("Enter a number to delete: ")
        habits.pop(int(delete_habit) - 1)
        with open("habits.txt", "w") as f:
            for user_habit in habits:
                f.write(user_habit["text"] + "|" + str(user_habit["status"]["completion"]) + "|" + str(user_habit["status"]["streak_count"]) + "\n")
    elif choice == "6":
        break
    else:
        print("Invalid choice, please try again.")