from random import randint

def play(word, lives):
    secret = []
    solution = ''
    for i in range(len(word)):
        if word[i] in ['-', ' ']:
            secret.append('')
            solution += (word[i])
        else:
            secret.append('_')
            solution += (word[i])
    print(' '.join(secret))
    print(solution)
    print(word)
    print(len(solution))
    print(len(secret))
    # main function
    pass


def display():
    # display word, reveal guessed letters
    pass


def word_set(set):
    # stores the letters of the word as a set
    pass


def guess():
    guess = input('Choose a letter: ')
    return guess
    # takes input
    pass


def lives():
    lives = 7
    return lives
    # counts lives and gives it to play() func as arg
    pass


def quit():
    # exit func

    pass

def choose_word(list):
    index = (randint(0, len(list)))
    return str(list[index][0])
    # chooses word and returns it as string


def scan_letter():
    
    # checks if letter is in word
    pass


def validate_guess():
    # might not need this
    pass


def play_log(set):
    # stores guesses
    pass


def store_file():
    list = []
    with open('countries-and-capitals.txt', 'r') as f:
        data = f.readlines()

    for line in data:
        words = line.split(' | ')
        list.append(words)
    return list
    # stores txt contents as a list (or two lists?)

play((choose_word(store_file())), lives())