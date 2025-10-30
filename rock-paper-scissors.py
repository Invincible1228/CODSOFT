import random

def play_game():
    user_score = 0
    computer_score = 0
    options = ['rock', 'paper', 'scissors']

    print("--- Welcome to Rock, Paper, Scissors! ---")

    while True:
        user_choice = input("Choose rock, paper, or scissors: ").lower()

        if user_choice not in options:
            print("Invalid choice. Please choose rock, paper, or scissors.")
            continue

        computer_choice = random.choice(options)

        print(f"\nYour choice: {user_choice}")
        print(f"Computer's choice: {computer_choice}\n")

        if user_choice == computer_choice:
            print("It's a tie!")
        elif (user_choice == 'rock' and computer_choice == 'scissors') or \
             (user_choice == 'scissors' and computer_choice == 'paper') or \
             (user_choice == 'paper' and computer_choice == 'rock'):
            print("You win this round! 🎉")
            user_score += 1
        else:
            print("Computer wins this round! 💻")
            computer_score += 1

        print(f"\n--- Score ---")
        print(f"You: {user_score} | Computer: {computer_score}")
        print("-------------")

        play_again = input("Do you want to play another round? (yes/no): ").lower()
        if play_again != 'yes':
            print("\nThanks for playing! Final score:")
            print(f"You: {user_score} | Computer: {computer_score}")
            break

if __name__ == "__main__":
    play_game()