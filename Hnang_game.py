import random

# List of words
words = ["python", "apple", "computer", "house", "garden"]

# Randomly select a word
word = random.choice(words)

# Store guessed letters
guessed_letters = []

# Number of wrong guesses allowed
max_attempts = 6
wrong_attempts = 0

print("=================================")
print("      WELCOME TO HANGMAN")
print("=================================")

# Game loop
while wrong_attempts < max_attempts:

    # Display current progress
    display_word = ""

    for letter in word:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "

    print("\nWord:", display_word)
    print("Wrong Attempts Left:", max_attempts - wrong_attempts)

    # Check win condition
    if "_" not in display_word:
        print("\n Congratulations!")
        print("You guessed the word:", word)
        break

    # Take user input
    guess = input("Enter a letter: ").lower()

    # Input validation
    if len(guess) != 1 or not guess.isalpha():
        print("Please enter only ONE alphabet letter.")
        continue

    # Check repeated guess
    if guess in guessed_letters:
        print("You already guessed that letter.")
        continue

    # Save guessed letter
    guessed_letters.append(guess)

    # Check correctness
    if guess in word:
        print(" Correct Guess!")
    else:
        wrong_attempts += 1
        print(" Wrong Guess!")

# Lose condition
if wrong_attempts == max_attempts:
    print("\n Game Over!")
    print("The word was:", word)