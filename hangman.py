import os
import random
import sys

def play_hangman():
    stages = [r'''
    +---+
    |   |
    O   |
   /|\  |
   / \  |
        |
    =========
    ''', r'''
    +---+
    |   |
    O   |
   /|\  |
   /    |
        |
    =========
    ''', r'''
    +---+
    |   |
    O   |
   /|\  |
        |
        |
    =========
    ''', r'''
    +---+
    |   |
    O   |
   /|   |
        |
        |
    =========
    ''', '''
    +---+
    |   |
    O   |
    |   |
        |
        |
    =========
    ''', '''
    +---+
    |   |
    O   |
        |
        |
        |
    =========
    ''', '''
    +---+
    |   |
        |
        |
        |
        |
    =========
    ''']

    # Load word list from a local file
    path = r'C:\Users\olueg\Documents\vs code\hangman\words'
    assert os.path.isfile(path)
    with open(path, "r") as f:
        pass

        word_list = f.read().splitlines()
    random_word = random.choice(word_list).lower()

    word_list = ["_" for _ in range(len(random_word))]
    stage = 6
    lives = 6

    # existing code...

    while True:
        guess = input("Guess a letter:").lower()
        if len(guess) != 1 or guess in word_list:
            print("Invalid input. Please enter a single letter that has not been guessed before.")
            continue

        found = False
        for letter in range(0, len(random_word)):
            if guess == random_word[letter]:
                word_list[letter] = guess
                found = True

        if not found:
            lives -= 1
            stage -= 1
            print("Wrong guess")
            print(stages[stage])

            if lives == 0:
                print("You lose")
                break

        print(' '.join(word_list))
        print(f"You have {lives} lives")

        if not "_" in word_list:
            print("You win")
            break
play_hangman()