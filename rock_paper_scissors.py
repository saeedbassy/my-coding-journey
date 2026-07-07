import random
computer_moves = ["rock", "paper", "scissors"]
keep_going = "yes"
while keep_going == "yes":
    computer_choice = random.choice(computer_moves)
    user_choice = input("Enter a move (rock/paper/scissors): ")
    print("The computer selected " + computer_choice + ".")
    if user_choice == computer_choice:
        print("You tied")
    elif user_choice == "rock" and computer_choice == "paper":
        print("You lose")
    elif user_choice == "rock" and computer_choice == "scissors":
        print("You win")
    elif user_choice == "paper" and computer_choice == "rock":
        print("You win")
    elif user_choice == "paper" and computer_choice == "scissors":
        print("You lose")
    elif user_choice == "scissors" and computer_choice == "rock":
        print("You lose")
    elif user_choice == "scissors" and computer_choice == "paper":
        print("You win")
    else:
        print("Invalid move!")
    keep_going = input("Play again? (yes/no): ")