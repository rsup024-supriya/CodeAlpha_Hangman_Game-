import random

words = ["python", "apple", "computer", "programming"]

word = random.choice(words)
guessed_letters = []
tries = 6

print("Welcome to Hangman Game!")

while tries > 0:
    display_word = ""

    for letter in word:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "

    print("\nWord:", display_word)

    if "_" not in display_word:
        print("Congratulations! You won!")
        break

    guess = input("Enter a letter: ").lower()

    if guess in guessed_letters:
        print("You already guessed that letter.")

    elif guess in word:
        print("Correct!")
        guessed_letters.append(guess)

    else:
        print("Wrong!")
        tries -= 1
        guessed_letters.append(guess)
        print("Tries left:", tries)

if tries == 0:
    print("You lost! The word was:", word)