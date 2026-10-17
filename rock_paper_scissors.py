
import random

print("================================")
print("   ROCK - PAPER - SCISSORS")
print("================================")

user_score = 0
computer_score = 0

while True:
    print("\nChoose your option:")
    print("1. Rock")
    print("2. Paper")
    print("3. Scissors")

    user_choice = input("Enter your choice: ").lower().strip()

    choices = ["rock", "paper", "scissors"]

    # Convert numeric input into a choice
    if user_choice == "1":
        user_choice = "rock"
    elif user_choice == "2":
        user_choice = "paper"
    elif user_choice == "3":
        user_choice = "scissors"

    if user_choice not in choices:
        print("Invalid choice! Please try again.")
        continue

    computer_choice = random.choice(choices)

    print("\nYour choice:", user_choice)
    print("Computer's choice:", computer_choice)

    if user_choice == computer_choice:
        print("Result: It's a tie!")

    elif (
        (user_choice == "rock" and computer_choice == "scissors")
        or (user_choice == "paper" and computer_choice == "rock")
        or (user_choice == "scissors" and computer_choice == "paper")
    ):
        print("Result: You win!")
        user_score += 1

    else:
        print("Result: You lose!")
        computer_score += 1

    print("\n----- SCOREBOARD -----")
    print("Your score:", user_score)
    print("Computer score:", computer_score)

    play_again = input("\nPlay again? (yes/no): ").lower().strip()

    if play_again != "yes":
        print("\n================================")
        print("         FINAL SCORE")
        print("================================")
        print("Your score:", user_score)
        print("Computer score:", computer_score)
        print("Thanks for playing!")

        if user_score > computer_score:
            print("Overall Winner: You!")
        elif computer_score > user_score:
            print("Overall Winner: Computer!")
        else:
            print("Overall Result: It's a tie!")

        break
