import random

while True:
    user_input = input("Enter your choice (rock, paper, scissors): ").lower()
    possible_choices = ["rock", "paper", "scissors"]
    computer_input = random.choice(possible_choices)
    
    if user_input not in possible_choices:
        print("Invalid choice! Please choose either rock, paper, or scissors.")
        continue

    print("User's choice is:", user_input)
    print("Computer's choice is:", computer_input)
    
    if user_input == computer_input:
        print("It's a tie as both selected the same choice:", user_input)
    elif user_input == "rock":
        if computer_input == "paper":
            print("Paper wins as paper covers the rock Computer wins!")
        else:
            print("Rock wins as rock breaks the scissors User wins!")
    elif user_input == "scissors":
        if computer_input == "paper":
            print("Scissors win as scissors cut the paper User wins!")
        else:
            print("Rock wins as rock breaks the scissors Computer wins!")
    elif user_input == "paper":
        if computer_input == "scissors":
            print("Scissors win as scissors cut the paper Computer wins!")
        else:
            print("Paper wins as paper covers the rock User wins!")
    
    play_again = input("Do you want to play again? (yes/no): ").lower()
    if play_again == "no":
        break
    else:
        print("Welcome again...!")  
print("Game Over...!")
