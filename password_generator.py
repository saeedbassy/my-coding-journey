import random
characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%"
random_password = []
password_length = input("Enter your password's desired length in characters: ")
def generate_password(characters):
    for i in range(1, int(password_length) + 1):
        random_password.append(random.choice(characters))
    user_password = "".join(random_password)
    return user_password
print("Your password is: " + generate_password(characters))