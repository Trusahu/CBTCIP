#Task 4 game codsoft
import random

def display_menu():
    print("\nWelcome to Rock-Paper-Scissors Game!")
    print("Choose your option:")
    print("1. Rock")
    print("2. Paper")
    print("3. Scissors")
    print("4. Exit")
    
def get_user_choice():
    while True:
        choice = input("\nEnter your choice (1-4): ").strip()
        if choice in ['1', '2', '3', '4']:
            return choice
        else:
            print("❌ Invalid choice! Please enter a number between 1 and 4.")

def get_computer_choice():
    choices = ['Rock', 'Paper', 'Scissors']
    return random.choice(choices)

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == 'Rock' and computer_choice == 'Scissors') or \
         (user_choice == 'Paper' and computer_choice == 'Rock') or \
         (user_choice == 'Scissors' and computer_choice == 'Paper'):
        return "You win!"
    else:
        return "You lose!"

def main():
    user_score = 0
    computer_score = 0
    rounds_played = 0

    display_menu() # Display the menu only once at the beginning

    while True:
        choice = get_user_choice()

        if choice == '4':
            print("Thank you for playing! Goodbye!")
            break

        user_choice = ['Rock', 'Paper', 'Scissors'][int(choice) - 1]
        computer_choice = get_computer_choice()

        print(f"\nYou chose: {user_choice}")
        print(f"Computer chose: {computer_choice}")

        result = determine_winner(user_choice, computer_choice)
        print(result)

        if result == "You win!":
            user_score += 1
        elif result == "You lose!":
            computer_score += 1
        
        rounds_played += 1

        print(f"\nScores after {rounds_played} round(s):")
        print(f"You: {user_score} | Computer: {computer_score}")

        while True:
            play_again = input("\nDo you want to play another round? (y/n): ").strip().lower()
            if play_again in ['y', 'n']:
                break
            else:
                print("❌ Invalid input! Please enter 'y' or 'n'.")
        
        if play_again != 'y':
            print("Thank you for playing! Goodbye!")
            break

if __name__ == "__main__":
    main()
