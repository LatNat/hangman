import os
from random import randint
import time
import sys
import string


boot_screen = '''	╔═════╤
	║
	║	    E X T R E M E
	║           h a n g m a n
	║
	║
_____╔═╩╩══════╗________________________'''
menu_screen1 = '''\r	╔═════╤
	║
	║
	║	   1 - I'm ready
	║	   2 - I have more important stuff to do 
	║	        
_____╔═╩╩══════╗________________________'''
menu_screen2 = '''\r	╔═════╤
	║
	║
	║	   1 - Warmup
	║	   2 - Let's do this!    
	║
_____╔═╩╩══════╗________________________'''


def easy_lives(tries, lives, guessthis):
    maxhp = lives
    hp = tries
    percentage = hp/maxhp
    disp = [f'''	╔═════╤
	║
	║
	║
	║         {guessthis}
	║
_____╔═╩╩══════╗________________________''',
f'''	╔═════╤
	║     |
	║
	║
	║         {guessthis}
	║
_____╔═╩╩══════╗________________________''',
f'''	╔═════╤
	║     O
	║    
	║     
	║         {guessthis}
	║
_____╔═╩╩══════╗________________________''',
f'''	╔═════╤
	║     O
	║     |
	║     
	║         {guessthis}
	║
_____╔═╩╩══════╗________________________''',
f'''	╔═════╤
	║     O
	║    /|
	║     
	║         {guessthis}
	║
_____╔═╩╩══════╗________________________''',
f'''	╔═════╤
	║     O
	║    /|\\
	║     
	║         {guessthis}
	║
_____╔═╩╩══════╗________________________''',
f'''	╔═════╤
	║     O
	║    /|\\
	║    /
	║         {guessthis}
	║
_____╔═╩╩══════╗________________________''',
f'''	╔═════╤
	║     O
	║    /|\\
	║    / \\
	║         {guessthis}
	║
_____╔═╩╩══════╗________________________''']
    if percentage >= 7/7:
        return disp[0]
    elif percentage <= 6/7 and percentage > 5/7:
        return disp[1]
    elif percentage <= 5/7 and percentage > 4/7:
        return disp[2]
    elif percentage <= 4/7 and percentage > 3/7:
        return disp[3]
    elif percentage <= 3/7 and percentage > 2/7:
        return disp[4]
    elif percentage <= 2/7 and percentage > 1/7:
        return disp[5]
    elif percentage <= 1/7:
        return disp[6]



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
            print("Don't come back")
            return False


# prints out menu screens, lets you choose difficulty, returns lives / or False (not yet used)


def game(gamestate=True):
    cls()
    while gamestate is True:                    # im bothered by this being on its own but might work anyway
        lives = menu()
        if lives is False:
            break
        if lives == 3:
            word = choose_word2(wordlist)
            play(word, lives)
        if lives == 7:
            word = choose_word(wordlist)        # if we include countries this needs to be renamed
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
    try:
        str(wordlist[index][0])
        return str(wordlist[index][0])
    except IndexError:
        choose_word(wordlist)


def choose_word2(wordlist):
    index = (randint(0, len(wordlist)))
    try:
        city = str(wordlist[index][1])
        return city[:-1]
    except IndexError:
        choose_word(wordlist)


# chooses a word, returns it as string


def encode(secret):
    return ' '.join(secret)


def display_letters(secret, word, guess):
    original_word = word
    word = word.lower()
    guess = guess.lower()
    for i in range(len(word)):
        if original_word[i] == guess.upper():
            secret[i] = guess.upper()
        elif word[i] == guess:
            secret[i] = guess
    return secret

def insult():
    insults = ['Lame...', 'Dude, please...', 'No comment', "I think you're a little slow","This is embarrassing","Not good. Not a surprise."]
    index = randint(0, 5)
    return insults[index]

def hypeman():
    hype = ["YEA GIMME THAT!", "WOOOOOOO!!!!", "YEA BABY!", "NOW THAT'S WHAT I CALL A LETTER!", "SKRRRRT!"]
    index = randint(0, 4)
    return hype[index]


def newgame():
    newgame = ''
    cls()
    newgame = input('New Game? Y/N\n')
    newgame = newgame.upper()   # asks for new game, if N: gamestate is false (might not work as intended)
    if newgame == 'Y':
        return True
    elif newgame == 'N':
        cls()
        print("Don't come back")
        time.sleep(2)
        return False


def play(word, lives):
    set_of_letters = set([i for i in word.lower() if i != ' '])
    tries = lives
    secret = ['_' if i != ' ' else ' ' for i in word]
    playlog = set()
    empty_set = set()
    valid_guesses = list(string.ascii_lowercase)
    while tries > 0:
        cls()
        guessthis = encode(secret)
        print(easy_lives(tries, lives, guessthis))
        if playlog == empty_set:
            print("You've already tried these: {}")
        else:
            print("You've already tried these: " + str(playlog))
        guess = input()
        if set_of_letters == empty_set or guess == word.lower():
            cls()
            print(f'''	╔═════╤       
	║        Your word was : {word}
	║                 
	║                 (FUCK YEAH!!!)            
	║             \O/ ˝
	║              |
_____╔═╩╩══════╗______/ \______________''')
            time.sleep(3)
            cls()
            print("You've won!")
            time.sleep(1.5)
            retry = newgame()
            if retry is False:
                sys.exit()
            else:
                game()     
        try:
            int(guess)
            print('This is a number you idiot')
            time.sleep(1.5)
            continue
        except ValueError:
            guess = guess.lower()
        if guess == 'quit':
            print("Don't come back")
            sys.exit()
        elif guess in ['í','ö','ü','ó','ú','ő','ű','á','é']:
            print('Do I look like I speak Hungarian?')
            time.sleep(1.5)
            continue
        elif len(guess) > 1 and guess != quit:
            print('Just one letter please')
            time.sleep(1.5)
            continue
        elif guess not in valid_guesses:
            print("You're not even trying...")
            time.sleep(1.5)
            continue
        elif guess in playlog:
            print("You've already tried this...")
            time.sleep(1.5)
            continue
        elif guess in set_of_letters:
            playlog.add(guess)
            secret = display_letters(secret, word, guess)
            set_of_letters.remove(guess)
            print(hypeman())
            time.sleep(1.5)
            continue
        else:
            tries -= 1
            playlog.add(guess)
            print(insult())
            time.sleep(1.5)
            continue
    cls()
    print(f'''	╔═════╤
	║     O    Your word was : {word}
	║    /|\\
	║    / \\
	║            YOU'RE STUPID!
	║
_____╔═╩╩══════╗________________________''')
    time.sleep(3)
    retry = newgame()
    if retry is False:
        sys.exit()
    
    # place of game over screen

# main play function. untouched.


wordlist = store_file()


# if gamestate is true the game runs. if its false, it quits. this is where the main menu needs to return a bool
# but i did not use it yet
# and we migh not need gamestate anyway
cls()
print(boot_screen)
time.sleep(3)
game()