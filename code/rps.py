import random

def get_user_choice():
    """Gets and validates the user's choice."""
    while True:
        user_choice = input("Choose Rock, Paper, or Scissors (R/P/S): ").upper()
        if user_choice in ['R', 'P', 'S']:
            return user_choice
        else:
            print("Invalid choice. Please choose R, P, or S.")

def get_computer_choice():
    """Generates a random choice for the computer."""
    return random.choice(['R', 'P', 'S'])

def determine_winner(user_choice, computer_choice):
    """Determines the winner of a round."""
    if user_choice == computer_choice:
        return "tie"
    elif (user_choice == 'R' and computer_choice == 'S') or \
         (user_choice == 'P' and computer_choice == 'R') or \
         (user_choice == 'S' and computer_choice == 'P'):
        return "user"
    else:
        return "computer"

def play_round():
    """Plays a single round of Rock Paper Scissors."""
    user_choice = get_user_choice()
    computer_choice = get_computer_choice()

    print(f"You chose: {user_choice}")
    print(f"Computer chose: {computer_choice}")

    winner = determine_winner(user_choice, computer_choice)

    if winner == "user":
        print("You win this round!")
    elif winner == "computer":
        print("Computer wins this round!")
    else:
        print("It's a tie!")
    return winner

if __name__ == "__main__":
    print("Welcome to Rock Paper Scissors!")
    play_round()
