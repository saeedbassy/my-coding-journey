contacts = []
choice = "0"

try:
    with open("contacts.txt", "r") as file:
        for contents in file.readlines():
            parts = contents.strip().split("|")
            contacts.append({"name": parts[0], "info": {"phone": parts[1], "city": parts[2]}})
except:
    pass

while choice != "5":
    print("1. Add a contact")
    print("2. View contacts")
    print("3. Search contacts by name")
    print("4. Delete a contact")
    print("5. Quit")
    choice = input("Choose a number: ")
    if choice == "1":
        user_name = input("Enter a name: ")
        user_phone = input("Enter a phone number: ")
        user_city = input("Enter a city: ")
        user_contact = {"name": user_name, "info": {"phone": user_phone, "city": user_city}}
        contacts.append(user_contact)
        with open("contacts.txt", "w") as f:
            for user_contact in contacts:
                f.write(user_contact["name"] + "|" + str(user_contact["info"]["phone"]) + "|" + user_contact["info"]["city"] + "\n")
    elif choice == "2":
        for user_contact in contacts:
            print(f"{user_contact["name"]}, {user_contact["info"]["phone"]}, {user_contact["info"]["city"]}")
    elif choice == "3":
        search_name = input("Enter a name to search for: ")
        for user_contact in contacts:
            if search_name.lower() in user_contact["name"].lower():
                print(f"{user_contact["name"]}, {user_contact["info"]["phone"]}, {user_contact["info"]["city"]}")
    elif choice == "4":
        for index, user_contact in enumerate(contacts):
            print(f"{index + 1}. {user_contact["name"]}, {user_contact["info"]["phone"]}, {user_contact["info"]["city"]}")
        delete_contact = input("Enter a number to delete: ")
        contacts.pop(int(delete_contact) - 1)
        with open("contacts.txt", "w") as f:
            for user_contact in contacts:
                f.write(user_contact["name"] + "|" + str(user_contact["info"]["phone"]) + "|" + user_contact["info"]["city"] + "\n")