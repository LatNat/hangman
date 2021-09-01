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


def iterate_guess(word, guess):
    stored_indexes = []
    for i in range(len(word)):
        if word[i] == guess:
            stored_indexes.append(i)
    return [stored_indexes, guess]


# def display_letters(stored_indexes, guess):
#   map()

# maybe use map() function?? could be right for us


def play(word, lives):
    set_of_letters = set(word)
    tries = lives
    secret = '_ '*(len(word))
    if set_of_letters == {}:
        cls()
        print("You've won!")
        newgame = input('New Game? Y/N')    # asks for new game, if N: gamestate is false (might not work as intended)
        if newgame == 'y'.upper():
            pass                            # don't know how to start new game (yet). skipping this for now
        elif newgame == 'n'.upper():
            global gamestate
            gamestate = False
            return gamestate
    playlog = set()
    while tries > 0:
        cls()
        print(secret)
        print(playlog)
        guess = input()
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
#        elif guess in set_of_letters:
#            playlog.add(guess)
#            iterate_guess(word, guess)
#            pass
        else:
            tries -= 1
            playlog.add(guess)
            print(playlog)
            continue


# main play function. untouched.

gamestate = True
wordlist = store_file()


# if gamestate is true the game runs. if its false, it quits. this is where the main menu needs to return a bool
# but i did not use it yet
# and we migh not need gamestate anyway


while gamestate is True:                    # im bothered by this being on its own but might work anyway
    lives = menu()
    if lives is False:
        break
    word = choose_word(wordlist)
    play(word, lives)
