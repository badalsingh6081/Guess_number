import random

def generate_secret_number():
    """Generate a random 4-digit number as the secret number."""
    return ''.join(random.sample('0123456789', 4))

def get_guess():
    """Get a guess from the player."""
    # while True:
    guess = input("Enter your guess (4 digits): ")
    if guess.isdigit() and len(guess) == 4:
        return guess
    else:
        print("Invalid input. Please enter a 4-digit number.")

def evaluate_guess(secret, guess):
    """Evaluate the guess and return the number of correct digits."""
    return sum(1 for s, g in zip(secret, guess) if s == g)

def play_mastermind():
    """Main function to play Mastermind."""
    print("Welcome to Mastermind!")

    # Player 1 sets the secret number
    secret_number = generate_secret_number()
    print("Player 1, you've set the secret number. Player 2, start guessing!")

    # Initialize variables
    attempts = 0

    # Game loop
    while True:
        # Player 2 guesses the number
        guess = get_guess()
        attempts += 1

        # Evaluate the guess
        correct_digits = evaluate_guess(secret_number, guess)

        # Check if the guess is correct
        if correct_digits == 4:
            print("Congratulations! Player 2 has guessed the number", secret_number, "in", attempts, "attempts.")
            break
        else:
            print("Player 2, you got", correct_digits, "digits correct. Try again!")

    # Player 2 is now Player 1
    print("Player 2, it's your turn to set the secret number. Player 1, start guessing!")

    # Player 1 sets the secret number
    secret_number = generate_secret_number()
    attempts = 0

    # Game loop
    while True:
        # Player 1 guesses the number
        guess = get_guess()
        attempts += 1

        # Evaluate the guess
        correct_digits = evaluate_guess(secret_number, guess)

        # Check if the guess is correct
        if correct_digits == 4:
            print("Congratulations! Player 1 has guessed the number", secret_number, "in", attempts, "attempts.")
            break
        else:
            print("Player 1, you got", correct_digits, "digits correct. Try again!")

# Start the game
play_mastermind()


