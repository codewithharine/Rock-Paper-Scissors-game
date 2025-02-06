import random

# Function to get the user's choice
def get_user_choice():
    user_choice = input("Enter rock, paper, or scissors (or type 'exit' to quit): ").lower()
    while user_choice not in ['rock', 'paper', 'scissors', 'exit']:
        print("Invalid input. Please enter 'rock', 'paper', 'scissors', or 'exit'.")
        user_choice = input("Enter rock, paper, or scissors (or type 'exit' to quit): ").lower()
    return user_choice

# Function to get the computer's choice
def get_computer_choice():
    return random.choice(['rock', 'paper', 'scissors'])

# Function to determine the winner
def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
         (user_choice == 'paper' and computer_choice == 'rock') or \
         (user_choice == 'scissors' and computer_choice == 'paper'):
        return "You win!"
    else:
        return "Computer wins!"

# Main function to play the game
def play_game():
    print("Welcome to Rock, Paper, Scissors!")
    
    while True:
        user_choice = get_user_choice()
        
        if user_choice == 'exit':
            print("Thank you for playing! Goodbye!")
            break
        
        computer_choice = get_computer_choice()

        print(f"\nYour choice: {user_choice}")
        print(f"Computer's choice: {computer_choice}")
        
        result = determine_winner(user_choice, computer_choice)
        print(result)

if __name__ == "__main__":
    play_game()
