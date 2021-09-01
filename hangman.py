from random import randint


def store_file():
    list = []
    with open('countries-and-capitals.txt', 'r') as f:
        data = f.readlines()

    for line in data:
        words = line.split(' | ')
        list.append(words)
    return list


def choose_word(wordlist):
    index = (randint(0, len(wordlist)))
    return str(wordlist[index][0])


def play(word, lives):
    set_of_letters = set(word)
    if set_of_letters == {}:
        print("You've won!")


wordlist = store_file()             # reads the txt file and stores it as a list

reference = choose_word(wordlist)   # reference is the word that needs to be guessed // might not need this
