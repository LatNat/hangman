import os
from random import randint
import time


menu_screen1 = '''\r1 - New Game
2 - Quit'''
menu_screen2 = '''\r1 - Easy
2 - Hard'''
# menu screens


def cls():
    os.system('cls' if os.name == 'nt' else 'clear')


# this function clears the screen. not necessary


def menu():
    cls()
    print(menu_screen1)
    cho = input()
    while True:
        if cho == '1':
            cls()
            print(menu_screen2)
            diff = input()
            if diff == '1':
                return 7
            elif diff == '2':
                return 3
        elif cho == '2':
            cls()
            print('goodbye')
            return False


# prints out menu screens, lets you choose difficulty, returns lives / or False (not yet used)


def game(gamestate=True):
    while gamestate is True:                    # im bothered by this being on its own but might work anyway
        lives = menu()
        if lives is False:
            break
        word = choose_word(wordlist)
        play(word, lives)


def store_file():
    list = []
    with open('countries-and-capitals.txt', 'r') as f:
        data = f.readlines()

    for line in data:
        words = line.split(' | ')
        list.append(words)
    return list

# opens txt, makes it a list


def choose_word(wordlist):
    index = (randint(0, len(wordlist)))
    return str(wordlist[index][0])


# chooses a word, returns it as string


def encode(secret):
    return ' '.join(secret)


def display_letters(secret, word, guess):
    word = word.lower()
    guess = guess.lower()
    for i in range(len(word)):
        if word[i] == guess:
            secret[i] = guess
    return secret


def newgame():
    newgame = ''
    cls()
    newgame = input('New Game? Y/N\n')
    newgame = newgame.upper()   # asks for new game, if N: gamestate is false (might not work as intended)
    if newgame == 'Y':
        return True
    elif newgame == 'N':
        cls()
        print('goodbye')
        time.sleep(2)
        return False


def play(word, lives):
    set_of_letters = set([i for i in word.lower() if i != ' '])
    tries = lives
    secret = ['_' if i != ' ' else ' ' for i in word]
    playlog = set()
    empty_set = set()
    while tries > 0:
        cls()
        print(encode(secret))
        print(playlog)
        print(word)
        print(set_of_letters)
        if set_of_letters == empty_set:
            cls()
            print("You've won!")
            time.sleep(1.5)
            gamestate = newgame()
            game(gamestate)
        guess = input()
        try:
            int(guess)
            print('this is a number you idiot')
            time.sleep(1.5)
            continue
        except ValueError:
            guess = guess.lower()
        if guess == 'quit':
            break
        elif len(guess) > 1 and guess != quit:
            print('just one letter pls')
            time.sleep(1.5)
            continue
        elif guess in playlog:
            print("you've already tried this...")
            time.sleep(1.5)
            continue
        elif guess in set_of_letters:
            playlog.add(guess)
            secret = display_letters(secret, word, guess)
            set_of_letters.remove(guess)
            continue
        else:
            tries -= 1
            playlog.add(guess)
            print(playlog)
            continue


# main play function. untouched.


wordlist = store_file()


# if gamestate is true the game runs. if its false, it quits. this is where the main menu needs to return a bool
# but i did not use it yet
# and we migh not need gamestate anyway


game()