import random


def choose_difficulty():
    print("\nSelect difficulty:")
    print("1. Easy (1-100)")
    print("2. Medium (1-500)")
    print("3. Hard (1-1000)")

    while True:
        choice = input("Enter choice (1/2/3): ").strip()
        if choice == "1":
            return "Easy", 100
        if choice == "2":
            return "Medium", 500
        if choice == "3":
            return "Hard", 1000
        print("Invalid choice. Please enter 1, 2, or 3.")


def number_guessing_game(player_name="Player", max_number=100, difficulty_name="Easy"):
    print("=" * 50)
    print("    PLAYER vs COMPUTER NUMBER GUESSING GAME")
    print("=" * 50)
    print(f"Difficulty: {difficulty_name} (1-{max_number})")
    print()
    
    # Computer picks a secret number
    computer_secret = random.randint(1, max_number)
    print(f"Computer has picked a secret number between 1-{max_number}!")
    print()
    
    # Player enters their secret number
    print(f"{player_name}, enter your secret number (1-{max_number})")
    print("(Computer won't see it!)")
    print()
    
    while True:
        try:
            player_secret = int(input(f"{player_name}, enter your secret number: "))
            if 1 <= player_secret <= max_number:
                break
            else:
                print(f"Please enter a number between 1 and {max_number}!")
        except ValueError:
            print("Invalid input! Please enter a valid number.")
    
    print("\n" * 3)
    print("=" * 50)
    print("        GAME STARTS - TAKE TURNS GUESSING")
    print("=" * 50)
    print()
    
    round_num = 1
    player_found = False
    computer_found = False
    computer_guesses = set()  # Track computer's guesses to avoid repeats
    computer_min = 1
    computer_max = max_number
    
    # Game loop
    while not player_found and not computer_found:
        print(f"--- ROUND {round_num} ---\n")
        
        # Player's turn to guess
        print(f"{player_name}'s turn to guess Computer's number")
        while True:
            try:
                player_guess = int(input(f"{player_name}, what's your guess? "))
                if 1 <= player_guess <= max_number:
                    break
                else:
                    print(f"Please enter a number between 1 and {max_number}!")
            except ValueError:
                print("Invalid input! Please enter a valid number.")
        
        print(f"{player_name} says: {player_guess}")
        
        if player_guess == computer_secret:
            print(f"{player_name} FOUND IT! The number was {computer_secret}!")
            player_found = True
        elif player_guess < computer_secret:
            print(f"Computer responds: My number is HIGHER than {player_guess}.")
        else:
            print(f"Computer responds: My number is LOWER than {player_guess}.")
        
        print()
        
        if player_found:
            break
        
        # Computer's turn to guess
        print(f"Computer's turn to guess {player_name}'s number")
        
        # Computer makes a bounded guess using previous feedback
        if computer_min > computer_max:
            print("Inconsistent hint state detected. Ending game.")
            break

        computer_guess = (computer_min + computer_max) // 2
        if computer_guess in computer_guesses:
            found = False
            for offset in range(1, max_number + 1):
                up = computer_guess + offset
                down = computer_guess - offset
                if up <= computer_max and up not in computer_guesses:
                    computer_guess = up
                    found = True
                    break
                if down >= computer_min and down not in computer_guesses:
                    computer_guess = down
                    found = True
                    break
            if not found:
                print("No valid computer guesses left. Ending game.")
                break

        computer_guesses.add(computer_guess)
        
        print(f"Computer says: {computer_guess}")
        
        if computer_guess == player_secret:
            print(f"Computer FOUND IT! The number was {player_secret}!")
            computer_found = True
        elif computer_guess < player_secret:
            print(f"{player_name} responds: My number is HIGHER than {computer_guess}.")
            computer_min = max(computer_min, computer_guess + 1)
        else:
            print(f"{player_name} responds: My number is LOWER than {computer_guess}.")
            computer_max = min(computer_max, computer_guess - 1)
        
        print()
        round_num += 1
    
    print("=" * 50)
    if player_found:
        print(f"{player_name} WINS!")
    else:
        print(f"Computer WINS!")
    print("=" * 50)


def main():
    print("Welcome to the Number Guessing Game!")
    print()
    
    # Get player name
    player_name = input("Enter your name (default: Player): ").strip() or "Player"
    
    while True:
        print("\n" * 2)
        difficulty_name, max_number = choose_difficulty()
        number_guessing_game(player_name, max_number=max_number, difficulty_name=difficulty_name)
        
        play_again = input("\nDo you want to play again? (yes/no): ").lower().strip()
        if play_again not in ['yes', 'y']:
            print("\nThanks for playing! Goodbye!")
            break


if __name__ == "__main__":
    main()
