import random

# Get player's name
name = input("Enter your name: ")
print(f"Welcome to Hangman, {name}!")

# Predefined words
words = ["apple", "banana", "cherry", "kiwi", "mango"]

# Pick a random word
word = random.choice(words)
guessed_word = ["_"] * len(word)  # List for underscores
attempts = 6  # Number of incorrect guesses allowed
guessed_letters = []  # Store guessed letters

print("Guess the word:", " ".join(guessed_word))

# Game loop
while attempts > 0 and "_" in guessed_word:
    guess = input("Enter a letter: ").lower()

    if len(guess) != 1 or not guess.isalpha():
        print("Please enter only a single letter.")
        continue

    if guess in guessed_letters:
        print("You already guessed that letter.")
        continue

    guessed_letters.append(guess)

    if guess in word:
        print("Good guess!")
        for i in range(len(word)):
            if word[i] == guess:
                guessed_word[i] = guess
    else:
        print("Wrong guess!")
        attempts -= 1

    print("Word:", " ".join(guessed_word))
    print("Attempts left:", attempts)
    print("Guessed letters:", " ".join(guessed_letters))

# Result
if "_" not in guessed_word:
    print(f"🎉 Congratulations {name}, you win! The word was: {word}")
else:
    print(f"💀 Sorry {name}, you lose! The word was: {word}")
