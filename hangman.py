import random

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

def main():

    path = "words.txt"
    with open(path) as f:
        word_list = f.read().splitlines()

    random_word = random.choice(word_list).lower()

    word_list = ["_" for _ in range(len(random_word))]
    stage = 7
    lives = 7

    while True:
        guess = input("Guess a letter: ").lower()
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
                print(f'"{random_word}" was the correct word')
                break

        print(' '.join(word_list))
        print(f"You have {lives} lives")

        if not "_" in word_list:
            print("You win")
            print(f'You guessed "{random_word}" correctly')
            break

main()