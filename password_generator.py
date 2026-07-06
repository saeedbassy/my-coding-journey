import random
def generate_password(characters):
        for i in range(1, int(password_length) + 1):
            random_password.append(random.choice(characters))
        user_password = "".join(random_password)
        return user_password
keep_going = "yes"
while keep_going == "yes":
    characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%"
    random_password = []
    password_length = input("Enter your password's desired length in characters: ")
    print("Your password is: " + generate_password(characters))
    keep_going = input("Generate other? (yes/no): ")