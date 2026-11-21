import random

# Predefined words
words = ["python", "computer", "program", "technology", "coding"]

# Select a random word
secret_word = random.choice(words)

guessed_letters = []
incorrect_guesses = 0
max_attempts = 6

print("=" * 35)
print("         HANGMAN GAME")
print("=" * 35)
print("Guess the hidden word one letter at a time.")
print("You have 6 incorrect attempts.")

while incorrect_guesses < max_attempts:

    # Display the current word
    display_word = ""

    for letter in secret_word:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "

    print("\nWord:", display_word)
    print("Incorrect guesses:", incorrect_guesses)
    print("Remaining attempts:", max_attempts - incorrect_guesses)

    # Check whether the word is completely guessed
    if all(letter in guessed_letters for letter in secret_word):
        print("\nCongratulations! You guessed the word:", secret_word)
        print("You won!")
        break

    guess = input("\nEnter a letter: ").lower().strip()

    # Validate input
    if len(guess) != 1 or not guess.isalpha():
        print("Please enter a single alphabet.")
        continue

    if guess in guessed_letters:
        print("You already guessed that letter.")
        continue

    guessed_letters.append(guess)

    if guess in secret_word:
        print("Correct guess!")
    else:
        print("Wrong guess!")
        incorrect_guesses += 1

else:
    print("\nGame Over!")
    print("The correct word was:", secret_word)

print("\nThank you for playing!")
