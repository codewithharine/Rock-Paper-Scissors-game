

# Rock, Paper, Scissors Game

## Overview
This is a simple Python-based **Rock, Paper, Scissors** game where you can play against the computer. The game allows continuous play, where you can keep playing rounds until you choose to exit by typing `exit`.

## Features
- **User Input**: You can choose between "rock", "paper", or "scissors" or type `exit` to quit the game.
- **Computer Choice**: The computer randomly picks one of the three options.
- **Winner Determination**: The game checks the conditions to declare if the user wins, the computer wins, or if it's a tie.
- **Continuous Play**: The game keeps running in a loop, allowing you to play multiple rounds until you type `exit`.

## Requirements
- Python 3.x

## Installation
1. Clone the repository or download the source code:
   ```bash
   git clone https://github.com/your-username/rock-paper-scissors-game.git
Usage
Start the app by running the Python script.
You will be prompted to enter your choice: rock, paper, or scissors.
The computer will randomly choose its option.
The winner of each round will be displayed, and you can choose to continue playing or type exit to quit the game.


Example
Welcome to Rock, Paper, Scissors!
Enter rock, paper, or scissors (or type 'exit' to quit): rock

Your choice: rock
Computer's choice: scissors
You win!

Enter rock, paper, or scissors (or type 'exit' to quit): paper

Your choice: paper
Computer's choice: rock
You win!

Enter rock, paper, or scissors (or type 'exit' to quit): exit
Thank you for playing! Goodbye!
Code Explanation
get_user_choice(): Prompts the user to enter their choice and ensures it's valid (either "rock", "paper", "scissors", or "exit").
get_computer_choice(): Randomly selects a choice for the computer.
determine_winner(): Compares the user's and computer's choices to determine the winner or if it's a tie.
play_game(): The main function that loops the game and allows continuous play until the user decides to exit.

