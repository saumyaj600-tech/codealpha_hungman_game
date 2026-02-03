import random

def hangman():
    # List of 5 predefined words
    words = ["python", "computer", "hangman", "programming", "challenge"]
    
    # Randomly select a word
    word = random.choice(words).upper()
    word_letters = set(word)  # Letters in the word
    guessed_letters = set()   # Letters guessed by user
    incorrect_guesses = 0
    max_incorrect = 6
    
    print("Welcome to Hangman!")
    print("You have 6 incorrect guesses allowed.")
    print("Word to guess:", " ".join(["_" if letter not in guessed_letters else letter for letter in word]))
    
    # Main game loop
    while incorrect_guesses < max_incorrect and word_letters - guessed_letters:
        print(f"\nIncorrect guesses: {incorrect_guesses}/{max_incorrect}")
        print("Guessed letters:", " ".join(sorted(guessed_letters)) if guessed_letters else "None")
        
        # Get user input
        guess = input("Guess a letter: ").upper()
        
        # Validate input
        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter.")
            continue
            
        if guess in guessed_letters:
            print("You already guessed that letter.")
            continue
            
        # Add guess to guessed letters
        guessed_letters.add(guess)
        
        # Check if guess is correct
        if guess in word_letters:
            print(f"Good guess! '{guess}' is in the word.")
        else:
            print(f"Sorry, '{guess}' is not in the word.")
            incorrect_guesses += 1
            
        # Display current word state
        current_word = " ".join([letter if letter in guessed_letters else "_" for letter in word])
        print("Word:", current_word)
    
    # Game over - check win/lose condition
    if word_letters - guessed_letters:
        print(f"\nGame Over! You ran out of guesses.")
        print(f"The word was: {word}")
    else:
        print(f"\nCongratulations! You guessed the word: {word}")

# Play again option
def main():
    while True:
        hangman()
        play_again = input("\nWould you like to play again? (y/n): ").lower()
        if play_again != 'y':
            print("Thanks for playing!")
            break

if __name__ == "__main__":
    main()