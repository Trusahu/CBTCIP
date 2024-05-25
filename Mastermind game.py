#12mastermind 

import random

def provide_feedback(guess, correct_number):
    correct_digits = sum(1 for a, b in zip(guess, correct_number) if a == b)
    
    if correct_digits == 0:
        print("Not quite the number. None of the digits are correct.")
    else:
        print(f"Not quite the number. But you did get {correct_digits} digit(s) correct!")
        correct_positions = ['X' if guess[i] != correct_number[i] else guess[i] for i in range(4)]
        print("Also these numbers in your input were correct.")
        print(' '.join(correct_positions))

def player_turn(player_number, correct_number):
    attempts = 0
    guessed_correctly = False
    
    while not guessed_correctly:
        guess = input(f"Player {player_number}, guess the 4 digit number: ")
        attempts += 1
        
        if guess == correct_number:
            if attempts == 1:
                print(f"Great! You guessed the number in just 1 try! You're a Mastermind, Player {player_number}!")
            else:
                print(f"Player {player_number}, you've become a Mastermind.\nIt took you only {attempts} tries.")
            guessed_correctly = True
        else:
            provide_feedback(guess, correct_number)
            print("Enter your next choice of numbers:")
    
    return attempts

def mastermind():
    # Generate random 4-digit numbers for Player 1 and Player 2
    correct_number_p1 = ''.join(random.choices('0123456789', k=4))
    correct_number_p2 = ''.join(random.choices('0123456789', k=4))
    
    print("Player 2, it's your turn to guess the number set by Player 1.")
    attempts_p2 = player_turn(2, correct_number_p1)
    
    print("\nPlayer 1, it's your turn to guess the number set by Player 2.")
    attempts_p1 = player_turn(1, correct_number_p2)
    
    if attempts_p1 < attempts_p2:
        print("Player 1 wins the game and is crowned Mastermind!")
    elif attempts_p2 < attempts_p1:
        print("Player 2 wins the game and is crowned Mastermind!")
    else:
        print("It's a tie!")

# Run the game
mastermind()
