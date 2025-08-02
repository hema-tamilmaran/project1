import random

# Predefined list of 5 words
word_list = ["apple", "tiger", "chair", "phone", "train","world","number","people"]

# Select a random word from the list
secret_word = random.choice(word_list)
guessed_letters = []
attempts_left = 6

# Display the current guessed word with _ for unknown letters
def display_word():
    return " ".join([letter if letter in guessed_letters else "_" for letter in secret_word])

print("Welcome to Hangman!")
print("Guess the word, one letter at a time.")
print(f"You have {attempts_left} incorrect guesses allowed.\n")

# Main game loop
while attempts_left > 0:
    print("Word: ", display_word())
    guess = input("Enter a letter: ").lower()

    # Check for valid single character input
    if len(guess) != 1 or not guess.isalpha():
        print(" Invalid input. Please enter a single letter.\n")
        continue

    if guess in guessed_letters:
        print("⚠ You already guessed that letter.\n")
        continue

    guessed_letters.append(guess)

    if guess in secret_word:
        print("✅ Good guess!\n")
        if all(letter in guessed_letters for letter in secret_word):
            print("🎉 Congratulations! You guessed the word:", secret_word)
            break
    else:
        attempts_left -= 1
        print(f"Incorrect! You have {attempts_left} tries left.\n")

else:
    print("💀 Game Over! The word was:", secret_word)