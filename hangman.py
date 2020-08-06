import random
import time
from os import system, name


def clear():
    if name == 'nt':
        # this is for windows
        system('cls')
    else:
        # this is for unix OS
        system('clear')  # Works only for linux


# The various stages of the hangman
hangman = [
    '''
    +---+
        |
        |
        |
       ===
''',
    '''
    +---+
    O   |
        |
        |
       ===
''',
    '''
    +---+
    O   |
    |   |
        |
       ===
''',
    '''
    +---+
    O   |
    |\\  |
        |
       ===
''',
    '''
    +---+
    O   |
   /|\\  |
        |
       ===
''',
    '''
    +---+
    O   |
   /|\\  |
     \\  |
       ===
''',
    '''
    +---+
    O   |
   /|\\  |
   / \\  |
       ===
''',
]

lives = len(hangman)-1  # number of lives of the hangman

word_file = open("words.txt")
# words.txt contains all English words, and I'm converting them to lowercase
# It should be in the same directory as hangman.py

words = word_file.read().split()  # Reading all the words
word = words[random.randint(0, len(words)-1)].lower()
# Choosing an English word and converting to lowercase

answer = ['_'] * len(word)
# This list of characters will be the partially hidden word
# that the user tries to complete by guessing


def game_over():
    clear()
    print("The answer was actually!!!")
    print("*Drum roll....*")
    time.sleep(2)

    print(word.title())
    # for i in range(len(word)):
    #     print(word[i], end='')
    # print('')
    if '_' in answer:
        print(hangman[-1])
        print("Hangman DIED!")
        print("Press F to pay respects")
    else:
        print("Well done, you got it correct. He lives to fight another day!")
        print("Press any key to quit")
    input()
    quit()


def bad_move():
    clear()
    print("That was a bad move.")
    print("Hangman is now one step closer to death")
    print("Be careful.....")
    input()


def good_move(move):
    clear()
    print("Nice thinking!")
    print("That was a good move.")

    for i in range(len(word)):
        if move == word[i]:
            answer[i] = move
    input()


def ask_move(played_moves):
    valid = False

    ch = ''
    while not valid:
        print("Enter an alphabet that you haven't tried before: ")
        ch = input()
        if ch.isalpha() and len(ch) == 1 and ch.lower() not in played_moves:
            valid = True
    return ch.lower()


def display(played_moves, lives_lost):
    clear()

    if lives_lost == lives:
        game_over()
    print("Lives left = ", lives-lives_lost-1)
    print(hangman[lives_lost])

    print("Used words: ", end='')
    print(played_moves)

    print("You current word:")
    print(answer[0].title(), end='')
    for i in range(1, len(answer)):
        print(answer[i], end='')
    print('')


def welcome():
    print("Hello there!")
    print("Welcome to the game of Hangman")
    print("Guess letters of a hidden word and prevent hangman from hanging")
    print("Ironic Lmao!")
    print("Press any key to start....")
    input()


def main():
    welcome()
    clear()
    lives_lost = 0
    played_moves = []
    while True:
        display(played_moves, lives_lost)
        move = ask_move(played_moves)
        played_moves.append(move)

        if move not in word:
            lives_lost += 1
            if lives_lost == lives:
                game_over()
            else:
                bad_move()
        else:
            good_move(move)
            if '_' not in answer:
                game_over()
        # game_over()


if __name__ == '__main__':
    main()
