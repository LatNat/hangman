def play(word, lives):
    # main function
    pass


def display():
    # display word, reveal guessed letters
    pass


def word_set(set):
    # stores the letters of the word as a set
    pass


def guess():
    # takes input
    pass


def lives():
    # counts lives and gives it to play() func as arg
    pass


def quit():
    # exit func

    pass

def choose_word():
    # chooses word and gives it to play() func as arg
    pass


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
    with open('countries-and-capitals.txt', 'r') as f:
        data = f.readlines()

    for line in data:
        words = line.split(' | ')
    
    # stores txt contents as a list (or two lists?)

store_file()