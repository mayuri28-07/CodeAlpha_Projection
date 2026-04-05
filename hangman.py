import random
words = ["python", "computer", "hangman", "programming", "developer"]
word = random.choice(words)
guessed_letters = []
attempts = 6

print("Welcome to Hangman Game!")
while attempts > 0:
    display_word = ""
    for letter in word:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "

    print("\nWord:", display_word)
    if "_" not in display_word:
        print("You Won!")
        break
    guess = input("Enter a letter: ").lower()
    if len(guess) != 1 or not guess.isalpha():
        print("Invalid input! Enter a single letter.")
        continue
    if guess in guessed_letters:
        print(" You already guessed that letter.")
        continue
    guessed_letters.append(guess)
    if guess in word:
        print("Correct guess!")
    else:
        attempts -= 1
        print(f" Wrong guess Attempts left: {attempts}")
if attempts == 0:
    print(f"You lost! The word was '{word}'")