import random


def choose_random_word():
    words = ["python", "hangman", "programming",
             "computer", "apple", "banana", "orange"]
    return random.choice(words)


def display_word(word, guessed_letters):
    displayed_word = ""
    for letter in word:
        if letter in guessed_letters:
            displayed_word += letter
        else:
            displayed_word += "_"
    return displayed_word


print("Welcome to Hangman!")
word_to_guess = choose_random_word()
guessed_letters = set()
max_attempts = 6
attempts = 0

while True:
    print("\n" + display_word(word_to_guess, guessed_letters))
    guess = input("Guess a letter: ").lower()

    if guess in guessed_letters:
        print("You've already guessed that letter.")
        continue

    guessed_letters.add(guess)

    if guess not in word_to_guess:
        attempts += 1
        print("Incorrect guess!")
        print(f"You have {max_attempts - attempts} attempts remaining.")

        if attempts >= max_attempts:
            print("Sorry, you lost! The word was:", word_to_guess)
            break
    elif "_" not in display_word(word_to_guess, guessed_letters):
        print("Congratulations! You guessed the word:", word_to_guess)
        break
