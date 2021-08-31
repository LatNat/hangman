import os
from random import randint

menu_screen1 = '''\r1 - New Game
2 - Quit'''
menu_screen2 = '''\r1 - Easy
2 - Hard'''

# menu screens

def cls():
    os.system('cls' if os.name=='nt' else 'clear')

# this function clears the screen. not necessary

def menu():
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


def play(word, lives):
    set_of_letters = set(word)
    if set_of_letters == {}:
        print("You've won!")

# main play function. untouched.


wordlist = store_file()
gamestate = True

# if gamestate is true the game runs. if its false, it quits. this is where the main menu needs to return a bool
# but i did not use it yet
# and we migh not need gamestate anyway


while gamestate is True:
    lives = menu()
    if lives is False:
        break
    word = choose_word(wordlist)

# running the game