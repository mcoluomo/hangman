import os
import random
import sys

def play_hangman():
    stages = ['''
    +---+
    |   |
    O   |
    /|\  |
    / \  |
        |
    =========
    ''', '''
    +---+
    |   |
    O   |
    /|\  |
    /    |
        |
    =========
    ''', '''
    +---+
    |   |
    O   |
    /|\  |
        |
        |
    =========
    ''', '''
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

    word_list = ["_"] * len(random_word)

    lives = 6

    while True:
        guess = input("Guess a letter:").lower()
        if len(guess) != 1 or guess in word_list:
            print("Invalid input. Please enter a single letter that has not been guessed before.")
        guess = input("Guess a letter:").lower()
        for letter in range(0, len(word_list)):
            if random_word[letter] == guess:
                word_list[letter] = guess
        if guess not in random_word:
            lives = lives - 1
            print("Wrong guess")
            
            if lives == 0:
                print("You lose")
                sys.exit()
        print(r' '.join(word_list))
        print(f"You have {lives} lives")

        if not "_" in word_list:
            print("You win")
            sys.exit()
play_hangman()